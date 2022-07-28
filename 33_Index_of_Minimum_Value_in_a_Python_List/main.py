def minmum(x):

    minmum_index = 0
    current_index = 1

    while current_index < len(x):

        if x[current_index] < x[minmum_index]:
            minmum_index = current_index
        current_index = current_index + 1

    return minmum_index


a = [23, 76, 45, 20, 70, 65, 15, 54, 100]
print(minmum(a))
