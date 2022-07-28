


with open(r"D:\Python_Prpjects\30_Count_Most_Frequent_Words_in_a_File\test.txt") as file:
    count = 0
    text = file.read()
    
    for i in text:
        if i.isupper():
            count += 1
    print(count)
