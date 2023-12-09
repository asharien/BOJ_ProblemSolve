import sys
N, M = map(str, sys.stdin.readline().rstrip().split())
NA, MA= list(map(int, N)), list(map(int, M))
print(sum(NA)*sum(MA))
