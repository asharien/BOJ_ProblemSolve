import sys
def FLIP(FLOP): return int(''.join((reversed(str(FLOP)))))
N, M = map(int, sys.stdin.readline().split())
print(FLIP(FLIP(N)+FLIP(M)))
