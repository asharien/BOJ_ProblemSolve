import sys
N = int(sys.stdin.readline())
TROPHY = [int(sys.stdin.readline()) for i in range(N)]
HISTORY, F, S = TROPHY[0], 1, 1
for i in TROPHY:
    if i > HISTORY: 
        F +=1
        HISTORY = i
HISTORY = TROPHY[-1]
for i in list(reversed(TROPHY)):
    if i > HISTORY: 
        S += 1
        HISTORY = i
print(F, S)
