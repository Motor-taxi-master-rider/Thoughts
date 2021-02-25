def simple_calculator(string: str) -> int:
    if not string:
        return 0

    stack = []
    i = len(string) - 1
    # 从右向左计算，否则 1-2+3将得错误结果-4
    while i > -1:
        if string[i].isdigit():
            # 将数字合并
            base = 1
            item = 0
            while i > -1 and string[i].isdigit():
                item += base * int(string[i])
                base *= 10
                i -= 1
            stack.append(item)
        elif string[i] == '(':
            # 计算至第一个右括号
            item = stack.pop()
            summary = 0
            positive = True
            while item != ')':
                if not isinstance(item, int):
                    if item == '+':
                        positive = True
                    else:
                        positive = False
                else:
                    if positive:
                        summary = summary + item
                    else:
                        summary = summary - item
                item = stack.pop()
            i -= 1
            stack.append(summary)
        else:
            stack.append(string[i])
            i -= 1

    summary = 0
    positive = True
    while stack:
        # 剩余栈中字符无括号
        item = stack.pop()
        if not isinstance(item, int):
            if item == '+':
                positive = True
            else:
                positive = False
        else:
            if positive:
                summary += item
            else:
                summary -= item
    return summary


assert simple_calculator('(1+(4+5+2)-3)+(6+8)') == 23
assert simple_calculator('1-2+3') == 2
