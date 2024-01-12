import sys
A, B = map(int, sys.stdin.readline().split())
CUSUM = [0 for i in range(B+5)]
CNT, i = 0, 0
while(CNT != B+1):
    i += 1
    for j in range(i):
        if(CNT == B+1): break
        CUSUM[CNT+1] = CUSUM[CNT]+i
        CNT += 1
print(CUSUM[B]-CUSUM[A-1])
