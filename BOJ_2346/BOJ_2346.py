import sys
from collections import deque
N = int(sys.stdin.readline())
L = list(map(int, sys.stdin.readline().split()))
D = deque([L[i], i+1] for i in range(len(L)))
X = []
while(D):
    TMP = D.popleft()
    X.append(TMP[1])
    if TMP[0]>0: D.rotate(1-TMP[0])
    else: D.rotate(-TMP[0])
print(*X)
