import sys
N, M = map(int, sys.stdin.readline().split())
FLOOR = []
HWOOD, VWOOD, SEQUENCE = 0, 0, 0
for _ in range(N):
    FLOOR.append(list(map(str, sys.stdin.readline().rstrip())))
for i in range(N):
    for j in range(M):
        if(FLOOR[i][j] == "-"): SEQUENCE = 1
        elif(FLOOR[i][j] == "|" and SEQUENCE == 1):
            HWOOD += SEQUENCE
            SEQUENCE = 0
        else: continue
    HWOOD += SEQUENCE
    SEQUENCE = 0
SEQUENCE = 0
for i in range(M):
    for j in range(N):
        if(FLOOR[j][i] == "|"): SEQUENCE = 1
        elif(FLOOR[j][i] == "-" and SEQUENCE == 1):
            VWOOD += SEQUENCE
            SEQUENCE = 0
        else: continue
    VWOOD += SEQUENCE
    SEQUENCE = 0
print(HWOOD+VWOOD)
