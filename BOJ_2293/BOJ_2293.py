import sys
N, K = map(int, sys.stdin.readline().split())
VAL = [int(sys.stdin.readline()) for i in range(N)]
CASETRACKER = {i:0 for i in range(K+1)}
CASETRACKER[0] = 1
for i in VAL:
    for _ in range(i, K+1): CASETRACKER[_] = CASETRACKER[_] + CASETRACKER[_-i]
print(CASETRACKER[K])
