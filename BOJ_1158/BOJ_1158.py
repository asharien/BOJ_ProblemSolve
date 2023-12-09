import sys
from collections import deque
N, K = map(int, sys.stdin.readline().split())
Y, ANS = deque([i+1 for i in range(N)]), []
while Y:
    Y.rotate(-K)
    ANS.append(Y.pop())
print("<", end='')
print(*ANS, sep=", ", end='')
print(">", end='')
