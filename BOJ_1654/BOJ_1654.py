import sys
K, N = map(int, sys.stdin.readline().split())
LANCABLE = [int(sys.stdin.readline()) for _ in range(K)]
LANCABLE.sort()
FLAG, BOTTOM_HOLDER = 0, 1
TOP_HOLDER = max(LANCABLE)
if(K == 1 and N == 1 or int((TOP_HOLDER+BOTTOM_HOLDER)/2) == 0):
    FLAG = 1
while(BOTTOM_HOLDER <= TOP_HOLDER and FLAG !=1):
    MID = int((TOP_HOLDER+BOTTOM_HOLDER)/2)
    CABLES = [int(i//MID) for i in LANCABLE]
    TOT = sum(CABLES)
    if(TOT<N):
        TOP_HOLDER = MID - 1
        CABLES.clear()
    elif(TOT>=N):
        ANS = MID
        BOTTOM_HOLDER = MID + 1
    else:
        CABLES.clear()
        TOP_HOLDER = MID -1

if(FLAG == 1):
    ANS = LANCABLE[0]
print(ANS)
