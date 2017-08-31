import re
import types
from collections import namedtuple
from functools import singledispatch


class Node:
    """简易数据结构构造父类"""
    _fields = []

    def __init__(self, *args):
        for name, value in zip(self._fields, args):
            setattr(self, name, value)


class Number(Node):
    """数字型"""
    _fields = ['value']


class BinOp(Node):
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
                left = BinOp(current.value, left)
                left.right = term()
            return left

        def term():
            left = pow()
            while accept('TIMES', 'DIVIDE'):
                left = BinOp(current.value, left)
                left.right = pow()
            return left

        def pow():
            left = factor()
            while accept('POWER'):
                left = BinOp(current.value, left)
                left.right = factor()
            return left

        def factor():
            if accept('NUM'):
                return Number(int(current.value))
            else:
                raise SyntaxError()

        return expr()

    def _evaluate(self, node):
        @singledispatch
        def visit(obj):
            raise NotImplemented

        @visit.register(BinOp)
        def _(node):
            """
            生成器。
            visit method for BinOp
            """
            left = yield node.left
            right = yield node.right
            # could be more dynamic
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
            visit生成器。
            返回输入数值及中间值。
            """
            result = visit(node)
            return (yield from result) if isinstance(result, types.GeneratorType) else result

        stack = [gen_visit(node)]  # 将跟节点的协程放入栈
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
    a = cal.caculate('1+2*4-5^2')
    print(a)
    b = cal.caculate('+'.join(str(i) for i in range(2017)))
    print(b)

if __name__ == '__main__':
    main()
