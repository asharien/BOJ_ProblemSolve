import sys
GAP = {'1':2, '0':4}
while(True):
    ANS = 0
    N = str(sys.stdin.readline().rstrip())
    if(N == '0'):break
    for i in N:
        if i in GAP: ANS += GAP[i]
        else: ANS += 3
    print(ANS+len(N)+1)
