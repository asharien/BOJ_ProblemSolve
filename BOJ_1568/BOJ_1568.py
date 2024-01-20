import sys
N = int(sys.stdin.readline())
TIMES, SING = 0, 1
while(True):
    if(N - SING <0):
        SING = 1
        TIMES += 1
        N -= SING
    else:
        N -= SING
        TIMES += 1
    SING += 1
    if(N == 0): break
print(TIMES)
