import sys
S, D, W = map(int, sys.stdin.readline().split())
X = ((S**2)/((D**2)+(W**2)))**0.5
print(int(X*D), int(X*W))
