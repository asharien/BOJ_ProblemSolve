import sys
N = int(sys.stdin.readline())
F = int(sys.stdin.readline())
MODIFIED = N-(N%100)
for i in range(100):
    if((MODIFIED+i)%F == 0):
        ANS = MODIFIED+i
        ANS = ANS%100
        break
if(ANS<10): print("0", ANS, sep='')
else: print(ANS)
