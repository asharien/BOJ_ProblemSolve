import sys
N = int(sys.stdin.readline())
for i in range(N):
    for j in range(1, N-i, 1):
        print(" ", end='')
    for k in range(i*2+1):
        print("*", end='')
    print()
