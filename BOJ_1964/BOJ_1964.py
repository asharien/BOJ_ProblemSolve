import sys
N = int(sys.stdin.readline())
X = (N**2)*3
Y = 5*N+2
ANS = (X+Y)//2
print(ANS%45678)
