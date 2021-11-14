import jieba

test_file = '../all_without_punctuation.txt'  # 测试语料
test_file3 = '../text_out_jieba.txt'  # 生成结果

with open(test_file, 'r', encoding='utf-8') as f:
    for line in f:
        seg = jieba.cut(line.strip().encode('utf-8'))
        s = '  '.join(seg)
        m = list(s)
        with open(test_file3, 'w') as f:
            for word in m:
                f.write(word)
