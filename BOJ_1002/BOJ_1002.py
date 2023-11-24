import sys
for _ in range(int(sys.stdin.readline())):
    X1,Y1,R1,X2,Y2,R2 = map(int, sys.stdin.readline().split())
    D = ((X1-X2)**2 + (Y1-Y2)**2)**0.5
    print("-1" if (X1, Y1, R1) == (X2, Y2, R2) else "0" if((X1, Y1) == (X2, Y2) and R1 != R2) else "1" if((R1+R2 == D) or (abs(R1-R2) == D) and ((X1, Y1) !=(X2, Y2))) else "2" if (abs(R1-R2)<D<R1+R2) and ((X1, Y1) !=(X2, Y2)) else "0")
