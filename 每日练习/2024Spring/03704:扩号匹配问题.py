while True:
    try:
        str = input()
        # 设置一个 stack 用来存放已经读入的左括号
        left_brackets = []

        # 设置一个返回的空字符列表,用来记录最后结果
        result = []

        # 从左往右扫描字符串
        for i in range(len(str)):
            # 如果是左括号，将左括号的索引值入栈，result 加上一个空格占位
            if str[i] == '(':
                left_brackets.append(i)
                result.append(' ')
            # 如果是右括号
            elif str[i] == ')':
                # 如果此时的左括号栈不为空，则弹栈表示当前右括号可以匹配成功，result 加上一个空格占位
                if len(left_brackets) != 0:
                    left_brackets.pop()
                    result.append(' ')
                # 否则当前右括号无法匹配，result 加上一个 ? 表示无法匹配的右括号
                else:
                    result.append('?')
            # 如果是字母，result 加上一个空格占位
            else:
                 result.append(' ')

        # 扫描结束后，left_brackets 剩余的就是无法匹配的左括号的索引
        # 逐个修改 result 对应索引的值
        for i in range(len(left_brackets)):
            result[left_brackets[i]] = '$'
        # 输出结果
        print(str)
        print(''.join(result))
    except EOFError:
        break