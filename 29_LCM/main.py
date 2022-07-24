import time

def least_common_multiple(n1, n2):

    x = 1

    while x <= (n1 * n2):

        if (x * n1) % n1 == 0 and (x * n1) % n2 == 0:

            print(x * n1)
            break
        
        else:
            x += 1
# ========================================================================


def least_common_multiple(a, b):
    if a > b:
        greater = a
    elif b > a:
        greater = b
    while(True):
        if ((greater % a == 0) and (greater % b == 0)):
            lcm = greater
            break
        greater = greater + 1
    print(lcm)


s = time.time()
least_common_multiple(11, 10)
e = time.time()

t = e - s

print(t)


# 0.0005214214324951172 him
