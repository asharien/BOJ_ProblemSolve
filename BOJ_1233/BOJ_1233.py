import sys
ANS = {}
A, B, C = map(int, sys.stdin.readline().split())
for i in range(1, A+1, 1):
    for j in range(1, B+1, 1):
        for k in range(1, C+1, 1):
            try: ANS[i+j+k] += 1
            except: ANS[i+j+k] = 1
print(max(ANS.keys(), key=(lambda k:ANS[k])))
