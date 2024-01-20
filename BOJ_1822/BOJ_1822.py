import sys
X = sys.stdin.readline()
N = set(list(map(int, sys.stdin.readline().split())))-set(list(map(int, sys.stdin.readline().split())))
print(len(N))
print(*sorted(N))
