import sys

N = int(sys.stdin.readline())
COUNT, COMB_EXTEND = 0, 1
while(1):
    COUNT += 1
    COMB_EXTEND = COUNT*6 + COMB_EXTEND
    if(COMB_EXTEND>=N):
        break
if(N == 1):
    print("1")
else:
    print(COUNT+1)
