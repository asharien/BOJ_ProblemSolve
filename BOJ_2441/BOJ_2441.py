import sys
N = int(sys.stdin.readline());
for i in range(0, N, 1):
    for k in range(0, i, 1):
        print(" ", end ='')
    for j in range(0, N-i, 1):
        print("*", end ='')
    print()
