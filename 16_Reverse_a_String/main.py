def reversing_string(string):

    string_list = []
    string_list_reversed = []

    for s in string:

        string_list.append(s)

    x = len(string_list)

    while x > 0:
        x -= 1
        string_list_reversed.append(string_list[x])

        string_reversed = "".join(string_list_reversed)

    return string_reversed.title()


print(reversing_string("ila ayhey"))

# ==========================================================================


def reverse_string(string):
    return string[::-1]


a = "lawrahK namA"
print(reverse_string(a))
