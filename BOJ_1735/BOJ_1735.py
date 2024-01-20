import sys
import math
N, M = map(int, sys.stdin.readline().split())
P, Q = map(int, sys.stdin.readline().split())
TEMP = math.lcm(M, Q)
X = (N*(TEMP//M)) + (P*(TEMP//Q))
Y = TEMP
QUICK = math.gcd(X, Y)
print(X//QUICK, Y//QUICK)
