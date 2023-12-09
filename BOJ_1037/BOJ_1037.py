import sys
LCM = []
CASE = int(sys.stdin.readline())
LCM = list(map(int, sys.stdin.readline().split()))
if(len(LCM) == 1): print(LCM[0]*LCM[0])
else: print(min(LCM)*max(LCM))
