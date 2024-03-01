# 设置一个辅助栈，用来模拟序列的真实压入弹出情况
# 先将待检测序列顺序压入主栈中，这样主栈的顺次 pop 得到的就是待检测序列
# 辅助栈将原始数据顺序压入栈，每次入栈后，检查循环当前栈顶元素是否与主栈栈顶元素相同
# 若相同说明真实情况中，此时应该弹栈了，不停比较两栈顶并弹栈，直至栈顶元素不同
# 辅助栈继续按照 1 -- n 的顺序接着入栈
# 最后检查辅助栈是否为空即可

original_str = input()
while True:
    try:
        seq = input()

        # 如果待检测序列长度与原始数据不相等，直接退出
        if len(seq) != len(original_str):
            print("NO")
            continue


        s1, s2 = [], []

        # 先将待检测序列逆序压入 s1
        for i in range(len(seq)):
            s1.append(seq[::-1][i])

        # 将原始数据顺序压入辅助栈
        for i in range(len(original_str)):
            # 入栈
            s2.append(original_str[i])

            # print("s2 压栈：")
            # print("s1:",s1)
            # print("s2:",s2)

            # 循环检测两个栈的栈顶元素是否相同
            # 一定要注意的是，只要 for 循环没结束 s1 中肯定还会有元素剩余
            # 但是 s2 可能中间过程中会为空，所以循环的条件要判空
            # 否则查看 s2 栈顶元素的行为可能会异常
            while (len(s2) != 0 and s1[-1] == s2[-1]):
                s1.pop()
                s2.pop()
                # print("s1 s2 弹栈")
                # print("s1:", s1)
                # print("s2:", s2)

        # 最后检查 s2 是否为空，若为空，则序列合法
        if (len(s2) == 0):
            print("YES")
        else:
            print("NO")
    except EOFError:
        break
