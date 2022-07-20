from collections import defaultdict


def group_elements_of_same_indices(elements):

    dfdict = defaultdict(list)

    for element in elements:

        for i, ele in enumerate(element):

            dfdict[i].append(ele)

    return list(dfdict.values())


elements = [[10, 20, 30], [40, 50, 60], [70, 80, 90, 100], ["yehya"]]

print(group_elements_of_same_indices(elements))

# ================================================================================

# inputLists = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
# outputLists = []
# index = 0

# for i in range(len(inputLists[0])):
#     outputLists.append([])
#     for j in range(len(inputLists)):
#         outputLists[index].append(inputLists[j][index])
#     index = index + 1
# a, b, c = outputLists[0], outputLists[1], outputLists[2]
# print(a, b, c)
