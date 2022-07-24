def common(input_data):
    duplicates = []
    result = []
    for word in input_data:
        if word not in result:
            result.append(word)
        elif word not in duplicates:
            duplicates.append(word)
    print(duplicates)
def find_duplicates(input_data) -> list:
    if type(input_data) == list:
        return common(input_data)
    elif type(input_data) == tuple:
        input_data = list(input_data)
        return common(input_data)
    elif type(input_data) == str:
        input_data = input_data.split()
        return common(input_data)


input_data = ["yehya", "alaa", "yehya", "adam", "adam", "yehya"]
input_data = ("yehya", "alaa", "yehya", "adam", "adam", "yehya")
input_data = "yehya ali yehya ali yehya adam"

find_duplicates(input_data)

# ========================================================================
# def find_duplicates(x):
#     length = len(x)
#     duplicates = []
#     for i in range(length):
#         n = i + 1
#         for a in range(n, length):
#             if x[i] == x[a] and x[i] not in duplicates:
#                 duplicates.append(x[i])
#     return duplicates


# names = ("Aman", "Akanksha", "Divyansha", "Devyansh",
#          "Aman", "Diksha", "Akanksha")
# print(find_duplicates(names))
