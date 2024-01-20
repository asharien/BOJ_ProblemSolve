import sys

def speedmodulo(A, B, C):
    if B == 1:
        return A%C
    else:
        TEMP = speedmodulo(A, B//2, C)
        if B % 2 == 0:
            return TEMP*TEMP%C
        else:
            return TEMP*TEMP*A%C



A, B, C = map(int, sys.stdin.readline().split( ))

print(speedmodulo(A, B, C))

