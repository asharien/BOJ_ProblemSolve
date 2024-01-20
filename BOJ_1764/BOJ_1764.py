import sys
NEVER_HEARD = set()
NEVER_SAW = set()
N, M = map(int, sys.stdin.readline().split())
for _ in range(N):
    NEVER_HEARD.add(str(sys.stdin.readline().rstrip()))
for _ in range(M):
    NEVER_SAW.add(str(sys.stdin.readline().rstrip()))
ANS = NEVER_HEARD & NEVER_SAW
print(len(ANS))
ANS = sorted(ANS)
for i in ANS:
    print(i)
