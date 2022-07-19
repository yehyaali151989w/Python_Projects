from collections import defaultdict


def group_anagrams(a):

    dfdict = defaultdict(list)

    for i in a:

        sorted_i = " ".join(sorted(i))

        dfdict[sorted_i].append(i)

    return f"{dfdict.keys()} => {dfdict.values()}"


words = ["tea", "eat", "bat", "ate", "arc", "car"]
print(group_anagrams(words))




