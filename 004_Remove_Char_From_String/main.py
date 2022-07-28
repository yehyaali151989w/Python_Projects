

# def remove_char_from_string(word, char):

#     word_list = []
    
#     for l in word:
        
#         if l != char.lower() and l != char.upper():
            
#             word_list.append(l)
            
#     word = "".join(word_list)
        
#     return word
# ======================================================
def remove_char_from_string(word, char):

    result = filter(lambda x: x != char.lower() and x != char.upper(), word)
    
    
    return "".join(result)
            



print(remove_char_from_string("ElzXxero wxexb scxhxoxoxl", 'x'))
print(remove_char_from_string("Elzdero wdedb scdhdododld", 'd'))
