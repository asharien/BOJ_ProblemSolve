import sys
A, B, C = map(int, sys.stdin.readline().split())
print("-1" if C<=B else A//(C-B)+1)
