import sys
N = int(sys.stdin.readline())
ANS = 0
for _ in range(N):
    ANS += int(sys.stdin.readline())
print(ANS-N+1)
