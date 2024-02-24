T = {'p': 23, 'e': 28, 'i': 33}


# 给定 days 天后，再过几天是 kind 高峰
def first_peak(kind, kind_days, days):
    if kind_days > days:
        while kind_days > days:
            kind_days -= T[kind]
    else:
        while kind_days <= days:
            kind_days += T[kind]
    return kind_days - days


if __name__ == '__main__':
    case = 1
    while True:
        p, e, i, d = map(int, input().split())
        if p == -1 and e == -1 and i == -1 and d == -1:
            break
        # 找到 d 天以后第一次 p 高峰
        p_first = first_peak('p', p, d)
        # 找到 d 天以后第一个 e 高峰
        e_first = first_peak('e', e, d)
        # 找到 d 天后第一个 i 高峰
        i_first = first_peak('i', i, d)

        k_p = 0
        while p_first + k_p * 23 <= 21252:
            if (p_first + k_p * 23 - e_first) % 28 == 0:
                k_i = 0
                while (p_first + k_p * 23 + k_i * 23 * 28) <= 21252:
                    if (p_first + k_p * 23 + k_i * 23 * 28 - i_first) % 33 == 0:
                        print(f'Case {case}: the next triple peak occurs in {p_first + k_p * 23 + k_i * 23 * 28} days.')
                        break
                    else:
                        k_i += 1
                break
            else:
                k_p += 1
        case += 1