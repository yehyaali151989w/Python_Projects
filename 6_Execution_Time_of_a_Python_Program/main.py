from time import time

start = time()


for i in range(0, 1000):
    
    print(i)

end = time()

execution_time = end - start

print(execution_time)

