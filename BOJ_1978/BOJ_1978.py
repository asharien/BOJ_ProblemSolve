import sys
import math
PRIME_NUMBER = []
FLAG = 0
N = int(sys.stdin.readline())
BOX = list(map(int, sys.stdin.readline().split()))
for x in BOX:
    if(x > 10000):
        if(x%2==0 or x%3==0 or x%4 == 0):
            x = 1
            FLAG = 1
    for i in range(2, int(math.sqrt(x))+1, 1):
        if(x == 1):
            FLAG = 1
            break
        elif(x == 2):
            FLAG = 0
            break
        elif(x == 3):
            FLAG = 0
            break
        elif(x%i == 0):
            if(x != i):
                FLAG = 1
            else:
                FLAG = 0
    if(FLAG == 1 or x == 1):
        FLAG = 0
        pass
    else:
        PRIME_NUMBER.append(x)
print(len(set(PRIME_NUMBER)))
