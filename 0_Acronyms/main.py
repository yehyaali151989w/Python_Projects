

user_input = input("Enter a Phrase: ")

text = user_input.split()

result = ""

for letter in text:

    result += letter[0].upper()

print(result)
