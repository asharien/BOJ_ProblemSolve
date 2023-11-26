import sys
from math import factorial
for _ in range(int(sys.stdin.readline())):
    N, M =map(int, sys.stdin.readline().split())
    print(factorial(M)//(factorial(M-N)*factorial(N)))
