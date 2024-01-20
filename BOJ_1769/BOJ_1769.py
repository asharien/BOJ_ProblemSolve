import sys
N = sum(list(map(int, sys.stdin.readline().rstrip())))
CNT, FIRST=1, N
while(N//10 != 0):
    TMP, RES = N, 0
    while(TMP !=0):
        RES += TMP%10
        TMP = TMP//10
    N = RES
    CNT += 1
print(CNT if FIRST//10 !=0 else CNT-1)
print("YES" if N%3 ==0 else "NO")
