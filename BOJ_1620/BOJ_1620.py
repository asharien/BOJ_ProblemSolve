import sys
N, M = map(int, sys.stdin.readline().split())
POKEDEX = {}
POKEDEX2 = {}
for _ in range(1,N+1,1):
    NAME = str(sys.stdin.readline().rstrip())
    POKEDEX[_] = NAME
    POKEDEX2[NAME] = _
for _ in range(M):
    TEMP = str(sys.stdin.readline().rstrip())
    if(TEMP.isdigit() == True): print(POKEDEX[int(TEMP)])
    else: print(POKEDEX2[TEMP])
