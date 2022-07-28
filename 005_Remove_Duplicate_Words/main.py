
# def remove_duplicates_words(sentence):
    
#     output_list = []
    
#     sentence_list = sentence.split()
    
#     for word in sentence_list:
        
#         if word not in output_list:
            
#             output_list.append(word)
            
#     return " ".join(output_list)
# ========================================================
# def remove_duplicates_words(sentence):

#     sentence_list = sentence.split()

#     unique_words = list(dict.fromkeys(sentence_list))

#     return " ".join(unique_words)

# =========================================================

def remove_duplicates_words(sentence):
    return " ".join(list(dict.fromkeys(sentence.split())))



print(remove_duplicates_words(
    "Hello Hello Elzero Elzero Web Web School School Hello"))

print(remove_duplicates_words(
    "yehya yehya alaa adam adam alaa alaa amir amir yehya"))
