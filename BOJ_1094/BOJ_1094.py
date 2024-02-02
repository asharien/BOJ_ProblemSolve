import sys
X = int(sys.stdin.readline())
STICK, ANS = [64, 32, 16, 8, 4, 2, 1], 0
while X>0:
    for i in STICK:
        if X>=i:
            X -=i
            ANS +=1
print(ANS)
