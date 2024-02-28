n, max_weight = map(int, input().split())
gift_info = {}

for i in range(n):
    value, weight = map(int, input().split())
    value_per_weight = value / weight
    gift_info[f"Gift_{i}"] = [value_per_weight, weight, value]

# 贪心算法，按照单价降序排列
sorted_gift = sorted(gift_info.values(), key=lambda x: x[0], reverse=True)

# 开始装包
current_weight = 0
total_value = 0
for gift in sorted_gift:
    if current_weight <= max_weight:
        if gift[1] <= max_weight - current_weight:
            current_weight += gift[1]
            total_value += gift[2]
        else:
            total_value += gift[0] * (max_weight - current_weight)
            break

print("{:.1f}".format(total_value))