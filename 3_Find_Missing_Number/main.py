

def find_missing_number(numbers):

    a = []

    for x in range(numbers[0], numbers[len(numbers) - 1]):

        a.append(x)

    a = set(a)

    numbers = set(numbers)

    r = a - numbers

    r = sorted(list(r))

    return r


numbers = [1, 2, 3, 4, 6, 7, 8, 9]

result = find_missing_number(numbers)

print(result)


# =====================================================================================

# def findMissingNumbers(n):
    
#     numbers = set(n)
#     length = len(n)
#     output = []
    
#     for i in range(1, length + 1):
#         if i not in numbers:
#             output.append(i)
#     return output


# listOfNumbers = [1, 2, 3, 5, 6, 7, 8, 9]
# print(findMissingNumbers(listOfNumbers))
