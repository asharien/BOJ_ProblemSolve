import sys
int(sys.stdin.readline())
G = list(map(int, sys.stdin.readline().split()))
print(len(G)-len(set(G)))
