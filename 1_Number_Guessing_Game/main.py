import random


def guess_number(start, end, max_tries):

    random_number = random.randint(start, end)

    print(random_number)

    guess_number = int(
        input(f"Enter any number between {start} and {end}: "))

    while guess_number != random_number:

        if max_tries > 1:

            if guess_number > random_number:

                print("Too hight")

            else:

                print("Too low")

            max_tries -= 1

            print(f"{max_tries if max_tries > 1 else 'the last'} trie(s) left")

            guess_number = int(input("Enter a number again: "))

        else:

            print("All tries finished! ")

            break

    else:
        print("Correct number :)")


try:
    guess_number(1, 100, 10)
except ValueError:
    print("The number you entered is not an integer!")

# =========================================================
# n = random.randrange(1, 10)
# guess = int(input("Enter any number: "))
# while n != guess:
#     if guess < n:
#         print("Too low")
#         guess = int(input("Enter number again: "))
#     elif guess > n:
#         print("Too high!")
#         guess = int(input("Enter number again: "))
#     else:
#       break
# print("you guessed it right!!")
