n, a, b = map(int, input().split())
need_water = list(map(int, input().split()))
Alice = 0
Bob = n - 1

# 记录两人水壶中剩余水量
Alice_water = a
Bob_water = b

# 两人补水次数
Alice_add_times = 0
Bob_add_times = 0

while Alice <= Bob:
    # 先处理两人给同一盆花浇水的情况
    if Alice == Bob:
        if Alice_water >= Bob_water:
            # Alice 浇水并向右移动
            if Alice_water >= need_water[Alice]:
                Alice_water -= need_water[Alice]
            else:
                Alice_water = a
                Alice_add_times += 1
                Alice_water -= need_water[Alice]
            Alice += 1
        else:
            # Bob 浇水并向左移动
            if Bob_water >= need_water[Bob]:
                Bob_water -= need_water[Bob]
            else:
                Bob_water = b
                Bob_add_times += 1
                Bob_water -= need_water[Bob]
            Bob -= 1
    else:
        # Alice 浇水并向右移动
        if Alice_water >= need_water[Alice]:
            Alice_water -= need_water[Alice]
        else:
            Alice_water = a
            Alice_add_times += 1
            Alice_water -= need_water[Alice]
        Alice += 1

        # Bob 浇水并向左移动
        if Bob_water >= need_water[Bob]:
            Bob_water -= need_water[Bob]
        else:
            Bob_water = b
            Bob_add_times += 1
            Bob_water -= need_water[Bob]
        Bob -= 1

print(Alice_add_times + Bob_add_times)