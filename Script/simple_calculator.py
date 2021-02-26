from typing import List, Union


def simple_calculator(string: str) -> float:
    postfix_list = postfix_expression(string)
    stack = []
    for item in postfix_list:
        if isinstance(item, int):
            stack.append(item)
        else:
            # 栈最上方的为第二位元素
            second = stack.pop()
            first = stack.pop()
            if item == '+':
                stack.append(first + second)
            elif item == '-':
                stack.append(first - second)
            elif item == '*':
                stack.append(first * second)
            elif item == '/':
                stack.append(first / second)

    return stack[-1]


def postfix_expression(string: str) -> List[Union[int, str]]:
    if not string:
        return []
    priority_map = {'+': 0, '-': 0, '*': 1, '/': 1}
    i = 0
    operator_stack = []
    postfix_expression = []
    while i < len(string):
        if string[i] == ' ':
            i += 1
            continue

        if string[i].isdigit():
            # 数字直接加入后缀表达式
            summary = 0
            while i < len(string) and string[i].isdigit():
                summary = summary * 10 + int(string[i])
                i += 1
            postfix_expression.append(summary)
        else:
            if string[i] == '(':
                # 若为左括号，入栈
                operator_stack.append(string[i])
            elif string[i] == ')':
                # 若为右括号，则把栈中运算符加入后缀表达式，直到遇到左括号
                operator = operator_stack.pop()
                while operator != '(':
                    postfix_expression.append(operator)
                    operator = operator_stack.pop()
            else:
                operator = string[i]
                if not operator_stack or operator_stack[-1] == '(' or priority_map[operator] > priority_map[
                    operator_stack[-1]]:
                    # 若1.栈空 2.栈顶元素为左括号 3.高于栈顶元素优先级，则入栈
                    operator_stack.append(operator)
                else:
                    # 若低于栈顶元素优先级，弹出栈顶加入后缀直到1.栈空 2.遇到左括号 3.遇到优先级比它低的运算符(乘和除，加和减之间的前后顺序)
                    while operator_stack and operator_stack[-1] != '(' and priority_map[operator] <= priority_map[
                        operator_stack[-1]]:
                        item = operator_stack.pop()
                        postfix_expression.append(item)
                    operator_stack.append(operator)

            i += 1

    while operator_stack:
        postfix_expression.append(operator_stack.pop())

    return postfix_expression


assert postfix_expression('11 + 22*( 33*44/55-66)-77/88') == [11, 22, 33, 44, '*', 55, '/', 66, '-', '*', '+', 77, 88,
                                                              '/', '-']
assert simple_calculator('(10-(15+6/2)/3)*(6+8)') == 56
assert simple_calculator('11 + 22*( 33*44/55-66)-77/88') == -861.075
