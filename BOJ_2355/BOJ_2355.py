import sys
A, B = map(int, sys.stdin.readline().split())
print((abs(A-B)+1)*(A+B)//2)
