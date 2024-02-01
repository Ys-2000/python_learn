from collections import Counter

# 假设你有一个列表 words
words = ["apple", "banana", "apple", "orange", "banana", "apple"]

# 使用 Counter 统计单词出现的次数
word_counts = Counter(words)
print(word_counts)
# # 打印统计结果
# for word, count in word_counts.items():
#     print(f"{word}: {count}")
