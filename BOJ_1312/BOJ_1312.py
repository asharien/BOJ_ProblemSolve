import sys
A, B, N = map(int, sys.stdin.readline().split())
TEMP = A%B
for _ in range(N-1):
    TEMP *= 10
    TEMP %= B
print(TEMP*10//B)
