import sys
CASE = int(sys.stdin.readline())
FIB = [0,1,1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
def FIBO(S: int):
    if(S <= 0):
        FIB[0] = 0
        return 0
    elif(S == 1):
        FIB[1] = 1
        return 1
    if(FIB[S] != 0): return FIB[S]
    else:
        FIB[S] = FIBO(S-1)+FIBO(S-2)
        return FIB[S]

for i in range(CASE):
    N = int(sys.stdin.readline())
    if(N == 0): print("1 0")
    elif(N == 1): print("0 1")
    elif(N ==2): print("1 1")
    else:
        FIBO(N)
        print(FIB[N-1], FIB[N])
