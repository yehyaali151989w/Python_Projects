

from functools import reduce
import numpy as np

# Mean


def calculate_mean(numbers):

    length = len(numbers)

    def calculate_sum(n1, n2):

        return n1 + n2

    sum = reduce(calculate_sum, numbers)

    mean = sum / length

    return mean


numbers = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]

print(calculate_mean(numbers))

print("+" * 100)
# =======================================================

# Median


def calculate_median(numbers):

    numbers = sorted(numbers)

    if len(numbers) % 2 != 0:

        median = numbers[int(np.floor(len(numbers) / 2))]
    else:

        median = (numbers[int((len(numbers) / 2) - 1)] +
                  numbers[int((len(numbers) / 2))]) / 2

    return median


numbers = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]

print(calculate_median(numbers))

print("+" * 100)
# =======================================================

# Mode
list1 = [12, 16, 20, 20, 16, 16, 20]
frequency = {}

for i in list1:

    frequency.setdefault(i, 0)

    frequency[i] += 1

frequent = max(frequency.values())

for i, j in frequency.items():

    if j == frequent:

        mode = i

print(mode)
