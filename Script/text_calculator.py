import re
import types
from collections import namedtuple
from functools import singledispatch
from inspect import Parameter, Signature


def make_signature(names):
    """用一个列表来产生参数签名的模块函数,也可以放在StructureMeta内部"""
    parameters = []
    #抓出参数的名称、默认值和注释
    parameter_re = re.compile(r'^(?P<name>\w+)(\s*=\s*(?P<default>\w+))?(\s*:\s*(?P<annotation>\w+))?$')
    for name in names:
        re_result = parameter_re.match(name)
        if not re_result:
            raise SyntaxError('Invalid parameter syntax：{}'.format(name))
        parameters.append(Parameter(kind=Parameter.POSITIONAL_OR_KEYWORD, **re_result.groupdict()))  #支持参数默认值和注释
    return Signature(parameters)


class StructureMeta(type):
    """
    Structure类的元类，在生成class的时候将_fields里提供的属性转化为
    参数签名类属性。
    """

    def __new__(cls, name, bases, clsdict):
        clsobj = super().__new__(cls, name, bases, clsdict)
        sig = make_signature(clsobj._fields)
        setattr(clsobj, '__signature__', sig)
        return clsobj


class Structure(metaclass=StructureMeta):
    """简易数据结构构造父类"""
    _fields = []

    def __init__(self, *args, **kwargs):
        # 这里实际上取的是self.__class___.__signature__
        bound = self.__signature__.bind(*args, **kwargs)
        for name, val in bound.arguments.items():
            setattr(self, name, val)


class Number(Structure):
    """数字型"""
    _fields = ['value']


class BinOp(Structure):
    """操作符号型"""
    _fields = ['op', 'left', 'right']


class Calculator:
    # 可以被tokenize函数解析的字符
    TOKENS = [
        r'(?P<NUM>\d+)',
        r'(?P<PLUS>\+)',
        r'(?P<MINUS>-)',
        r'(?P<TIMES>\*)',
        r'(?P<DIVIDE>/)',
        r'(?P<POWER>\^)',
        r'(?P<WS>\s+)',
    ]

    # 储存字符类型和值的元组
    Token = namedtuple('Token', ['type', 'value'])

    def __init__(self, token=None):
        if token:
            self.TOKENS = token
        # 预编译正则表达式
        self.MASTER_RE = re.compile('|'.join(self.TOKENS))

    def caculate(self, text):
        """解析并计算表达式"""
        self.text = text
        try:
            token = self._tokenize(text)
            tree = self._parse(token)
            result = self._evaluate(tree)
        except Exception as e:
            raise e
        return result

    def _tokenize(self, text):
        """从字符串开始扫描所有匹配字符,输出所有非空元素"""
        try:
            scan = self.MASTER_RE.scanner(text)
        except Exception as  e:
            raise e
        return (self.Token(m.lastgroup, m.group())
                for m in iter(scan.match, None)
                if m.lastgroup != 'WS')

    def _parse(self, toks):
        """将tokenize后的元素parse成树结构"""
        lookahead, current = next(toks, None), None

        def accept(*toktypes):
            """判断生成器toks的下个元素是否为传入类型"""
            nonlocal lookahead, current
            if lookahead and lookahead.type in toktypes:
                current, lookahead = lookahead, next(toks, None)
                return True

        # 表达式结构：
        # expr ::= term { +|- term }*
        # term ::= pow { *|/ pow}*
        # pow  ::= factor { ^ factor}*
        # factor ::= NUM
        def expr():
            left = term()
            while accept('PLUS', 'MINUS'):
                left = BinOp(current.value, left, factor())
            return left

        def term():
            left = pow()
            while accept('TIMES', 'DIVIDE'):
                left = BinOp(current.value, left, factor())
            return left

        def pow():
            left = factor()
            while accept('POWER'):
                left = BinOp(current.value, left, factor())
            return left

        def factor():
            if accept('NUM'):
                return Number(int(current.value))
            else:
                raise SyntaxError('Invalid character.')

        return expr()

    def _evaluate(self, node):
        """遍历生成树计算结果"""

        @singledispatch
        def visit(obj):
            raise NotImplemented

        @visit.register(BinOp)
        def _(node):
            """
            协程。
            visit method for BinOp
            """
            left = yield node.left
            right = yield node.right
            # TODO: could be more dynamic
            switch = {
                '+': lambda x, y: x + y,
                '-': lambda x, y: x - y,
                '*': lambda x, y: x * y,
                '/': lambda x, y: x / y,
                '^': lambda x, y: x ** y,
            }
            try:
                return switch.get(node.op, None)(left, right)  # 产生StopIteration并返回结果
            except TypeError as e:
                print('Error in syntax.')

        @visit.register(Number)
        def _(node):
            """visit method for number"""
            return node.value

        def gen_visit(node):
            """
            委派生成器。
            返回输入数值及中间值。
            """
            result = visit(node)
            # 非常tricky的写法
            return (yield from result) if isinstance(result, types.GeneratorType) else result

        stack = [gen_visit(node)]  # 将根节点的协程放入栈
        result = None
        while stack:
            try:
                node = stack[-1].send(result)  # send(None)预激协程，send（result）将计算好的值存入协程
                stack.append(gen_visit(node))  # 深度遍历添加协程，等待处理
                result = None
            except StopIteration as e:
                stack.pop()
                result = e.value  # 取得number的值或表达式计算值
        return result


def main():
    cal = Calculator()
    a = cal.caculate('1+2*4-5')
    print(a)
    b = cal.caculate('+'.join(str(i) for i in range(2017)))  # 超深栈计算
    print(b)


if __name__ == '__main__':
    main()
