import sys 
from math import inf as INF
def LOOK(N):
    FIX = 0
    for i in str(N):
        if(i != '4' and i != '7'):
            FIX = INF
            break
    return FIX
N= int(sys.stdin.readline().rstrip())
while(True):
    TMP = LOOK(N)
    if(TMP == 0):break
    else: N -=1
print(N)
