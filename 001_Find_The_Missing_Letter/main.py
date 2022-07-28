import string



def find_missing_letter(given_sring):

    letters = string.ascii_lowercase
    
    start = letters.find(given_sring[0])
    
    for letter in letters[start:]:
        
        if letter not in given_sring:
            
            return letter

    return "No missing letter found."

print(find_missing_letter("abcdegh"))
print(find_missing_letter("mnoqrstuvw"))
print(find_missing_letter("xyz"))
    
    