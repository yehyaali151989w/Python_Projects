from collections import Counter

words = []

with open(r"D:\Python_Prpjects\30_Count_Most_Frequent_Words_in_a_File\test.txt", "r") as f:
    for line in f:
        words.extend(line.split())

counts = Counter(words)

top5 = counts.most_common(5)
print(top5)
