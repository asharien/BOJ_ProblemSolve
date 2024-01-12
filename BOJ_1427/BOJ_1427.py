import sys
N = list(sys.stdin.readline().rstrip())
N.sort()
print(*list(reversed(N)), sep="")
