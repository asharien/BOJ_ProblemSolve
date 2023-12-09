import sys
CASE = int(sys.stdin.readline())
ANS = 0
F = list(map(int, sys.stdin.readline().split()))
S = list(map(int, sys.stdin.readline().split()))
F = sorted(F)
S = sorted(S, reverse = True)
for _ in range(CASE):
    ANS += F[_]*S[_]
print(ANS)
