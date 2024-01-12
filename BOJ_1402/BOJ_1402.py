import sys
CASE = int(sys.stdin.readline())
for i in range(CASE):
    X, Y = map(int, sys.stdin.readline().split())
    if(X<=Y):
        print("yes")
    elif(X>=Y):
        print("yes")
    else:
        print("no")
