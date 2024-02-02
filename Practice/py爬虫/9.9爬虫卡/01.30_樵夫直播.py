from collections import Counter
import jieba

# 假设你有一个列表 words
# words = ["apple", "banana", "apple", "orange", "banana", "apple"]
# words = ['常规赛', '今日', '点播', '努力', '幸运', '全民', '街篮', '龙凤呈祥', '版本', '上线']

# 读取文本文件
with open('text.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# 分词
words = list(jieba.cut(text))

# 统计词频
word_counts = Counter(words)

wordlist = []
for line in word_counts:
    textlist = line.split()
    for word in textlist:
        if len(word)>=2:
            wordlist.append(word)


print(wordlist[:10])
# # 获取出现次数最多的前 10 个词
# top_10_words = word_counts.most_common(10)
#
# # 打印结果
# print("出现次数最多的前10个词：")
# for word, count in top_10_words:
#     print(f"{word}: {count}")


# # 使用 Counter 统计单词出现的次数
# word_counts = Counter(words)
# print(word_counts)
# # # 打印统计结果
# # for word, count in word_counts.items():
# #     print(f"{word}: {count}")





