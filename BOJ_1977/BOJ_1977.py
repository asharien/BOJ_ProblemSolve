import sys
M = int(sys.stdin.readline())
N = int(sys.stdin.readline())
ANS = []
for i in range(M, N+1):
    if int(i**0.5) == i**0.5: ANS.append(i)
if len(ANS) !=0: print(sum(ANS), min(ANS), sep='\n')
else: print("-1")
