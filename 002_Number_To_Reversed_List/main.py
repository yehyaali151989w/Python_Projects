

def convert(numbers):
    
    # o = []
    # s = str(numbers)

    # for n in s:
    #     o.append(int(n))
    
    # return o[::-1]
    
    return [int(n) for n in str(numbers)[::-1]]
      

print(convert(987654321))
print(convert(54321))
print(convert(876543))
