while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    # 初始化队列，将所有序号按序加入队列
    queue = [x for x in range(1, n + 1)]

    call_num = 1

    # 开始循环报数
    while (len(queue) != 1):
        # 先从队列头部弹出来一个人报数，是 m 就不再加入队列，不是 m 就再放回队尾
        caller = queue.pop(0)
        if call_num != m:
            queue.append(caller)
            call_num += 1
        else:
            call_num = 1

    print(queue[0])
