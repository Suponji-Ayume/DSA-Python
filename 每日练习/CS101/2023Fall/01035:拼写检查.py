def similar(query_word, dic_lst):
    # 存放与该单词相似的所有单词列表
    result_lst = []
    for dic_word in dic_lst:
        # 如果长度相差大于 1，一定不相似
        if abs(len(query_word) - len(dic_word)) > 1:
            continue
        # 如果长度相等，则比较差异数
        elif len(query_word) == len(dic_word):
            diff_num = sum(1 for i, j in zip(query_word, dic_word) if i != j)
            if diff_num == 1:
                result_lst.append(dic_word)
        # 如果长度相差 1，尝试略去长单词的每一个字符后再和短单词比较，看是否相等
        else:
            long_word, short_word = (query_word, dic_word) if len(query_word) > len(dic_word) else (
                dic_word, query_word)
            for i in range(len(long_word)):
                # 特判一下只有末尾多一个字符的情况，否则会有数组索引越界的报错
                if i == len(long_word) - 1:
                    if long_word[:-1] == short_word:
                        result_lst.append(dic_word)
                        break
                else:
                    if long_word[:i] + long_word[i + 1:] == short_word:
                        result_lst.append(dic_word)
                        break
    return result_lst


if __name__ == '__main__':
    # 输入词典
    dic_lst = []
    while True:
        dic_word = input()
        if dic_word == '#':
            break
        else:
            dic_lst.append(dic_word)

    # 输入要查询的词
    while True:
        query_word = input()
        if query_word != '#':
            if query_word in dic_lst:
                print(f'{query_word} is correct')
            else:
                if len(similar(query_word, dic_lst)) == 0:
                    print(f'{query_word}:')
                else:
                    print(f"{query_word}:", " ".join(similar(query_word, dic_lst)))
        else:
            break
