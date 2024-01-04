import sys
import math
NOT_PRIME = []
PRIME_JUMPER = 2
START, END = map(int, sys.stdin.readline().split())
for i in range(PRIME_JUMPER, round(math.sqrt(END))+1):
    JUMPER = START//i**2
    while JUMPER * (i**2) <=END:
        if(JUMPER *(i**2)-START >=0 and JUMPER *(i**2) - START <=END-START):
            NOT_PRIME.append(JUMPER*(i**2))
        JUMPER += 1
NOT_PRIME = set(NOT_PRIME)
NOT_PRIME = list(NOT_PRIME)
print(END-START-len(NOT_PRIME)+1)
