
def longest_word(sentence):
    
    maximum_index = 0
    current_index = 1
    sentence = sentence.split(' ')
    
    while current_index < len(sentence):
        
        if len(sentence[current_index]) > len(sentence[maximum_index]):
            
            maximum_index = current_index
            
        current_index += 1
        
    return sentence[maximum_index]


print(longest_word("yehya ali alaa miiiiiiiiiiiiiiii"))
print(longest_word("I love you toooooooooooooooooo much"))
