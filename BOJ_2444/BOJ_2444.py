from sys import stdin
N = int(stdin.readline())
N = int(2*N)
S = int((N//2))
for i in range(0, S, 1):
    for j in range(i, S-1, 1):
        print(" ", end = "")
    for k in range(0, i*2+1, 1):
        print("*", end = "")
    print("")

for i in range(S-1, 0, -1):
    for j in range(S-1, i-1, -1):
        print(" ", end = "")
    for k in range(i*2-1, 0, -1):
        print("*", end = "")
    print("")
