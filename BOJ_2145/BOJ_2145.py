import sys
def LINESUM(N):
    X = 0
    while(N !=0):
        X += N%10
        N = N//10
    if(len(str(X))>=2): return LINESUM(X)
    else: return X

while(True):
    N = int(sys.stdin.readline())
    if(N == 0):break
    else:
        X = LINESUM(N)
        print(X)
