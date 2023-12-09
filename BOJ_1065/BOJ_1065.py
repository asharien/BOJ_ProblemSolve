import sys
N, ANS = int(sys.stdin.readline()), 99
if(N<100): print(N)
else:
    for i in range(100, N+1, 1):
        if(i%10-(i%100//10) == (i%100//10)-i//100):ANS+=1
    print(ANS)
