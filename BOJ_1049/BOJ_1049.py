import sys
N, M = map(int, sys.stdin.readline().split())
ANS, BRAND, SINGLE = [], [], []
for _ in range(M):
    P, S = map(int, sys.stdin.readline().split())
    BRAND.append(P)
    ANS.append(S*N)
    SINGLE.append(S)
LW, BP, RM = min(SINGLE), N//6, N-(N//6)*6
for i in BRAND:
    ANS.append(BP*i+RM*LW)
    ANS.append((BP+1)*i)
print(min(ANS))
