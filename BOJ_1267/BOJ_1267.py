import sys
import math
M = []
Y = []
N = int(sys.stdin.readline())
RECORD = list(map(int, sys.stdin.readline().split()))
for i in RECORD:
    if(i%30 == 0):
        Y.append(((i/30) + 1)*10)
    elif(i%30 !=0):
        Y.append(math.ceil(i/30)*10)
    if(i%60 == 0):
        M.append(((i/60) + 1)*15)
    elif(i%60 != 0):
        M.append(math.ceil(i/60)*15)
if(sum(Y) == sum(M)): print(f'Y M {sum(Y):.0f}')
elif(sum(Y)<sum(M)): print(f'Y {sum(Y):.0f}')
elif(sum(M)<sum(Y)): print(f'M {sum(M):.0f}')
