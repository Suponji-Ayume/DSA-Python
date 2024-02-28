# 前缀表达式的计算机求值：
# 从右至左扫描表达式，遇到数字时，将数字压入堆栈，遇到运算符时，弹出栈顶的两个数，用运算符对它们做相应的计算（栈顶元素 和 次顶元素）
# 将结果入栈
# 重复上述过程直到表达式最左端，最后运算得出的值即为表达式的结果

def calculate(expression):
    # 创建一个空 stack
    stack = []

    # 先将表达式按空格分隔
    splited_expression = list(expression.split())
    if len(splited_expression) == 0:
        return 0

    # 从右向左扫描表达式
    for element in splited_expression[::-1]:
        # 将数字压入栈
        if element in ['+', '-', '*', '/']:
            num1 = stack.pop()
            num2 = stack.pop()
            if element == "+":
                stack.append(num1 + num2)
            elif element == '-':
                stack.append(num1 - num2)
            elif element == '*':
                stack.append(num1 * num2)
            else:
                stack.append(num1 / num2)
        else:
            stack.append(float(element))
    return stack[0]

if __name__ == '__main__':
    expression = input()
    print("%f" % calculate(expression))