import sys
ANS, PLACE_HOLDER = 0, 0
for _ in range(10):
    N, M = map(int, sys.stdin.readline().split())
    ANS -= N
    ANS += M
    if(ANS>PLACE_HOLDER):PLACE_HOLDER = ANS
print(PLACE_HOLDER)
