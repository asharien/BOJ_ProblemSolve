import sys
for _ in range(int(sys.stdin.readline())):
    X, Y = map(int, sys.stdin.readline().split())
    print(int((4*(Y-X)-1)**0.5))
