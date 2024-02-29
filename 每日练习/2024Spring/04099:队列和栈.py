n = int(input())
for _ in range(n):
    stack = []
    queue = []
    m = int(input())
    error = False
    for __ in range(m):
        instruction = input().split()
        # push 操作
        if len(instruction) == 2:
            queue.append(instruction[1])
            stack.append(instruction[1])
        # pop 操作
        else:
            if len(queue) == 0:
                error = True
            else:
                queue.pop(0)
                stack.pop()

    # 如果中间过程报错
    if error == True:
        print("error")
        print("error")
    # 如果最后全空
    else:
        if len(queue) == 0:
            print()
            print()

        else:
            # 输出 queue
            for i in range(len(queue)):
                if i != len(queue) - 1:
                    print(queue[i], end=" ")
                else:
                    print(queue[i])
            # 输出 stack
            for i in range(len(stack)):
                if i != len(stack) - 1:
                    print(stack[i], end=" ")
                else:
                    print(stack[i])
