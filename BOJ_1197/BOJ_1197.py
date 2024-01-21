import sys
#Practice Kruskal Sample Code
V, E = map(int, sys.stdin.readline().split())
SN, EL, ANS = [i for i in range(V+1)], [], 0
for _ in range(E): EL.append(list(map(int, sys.stdin.readline().split())))
EL.sort(key=lambda X:X[2])
def SEARCH(N):
    if N!= SN[N]:SN[N]=SEARCH(SN[N])
    return SN[N]
for START, END, WEIGHT in EL:
    BASE_ROOT = SEARCH(START)
    FINAL_ROOT = SEARCH(END)
    if BASE_ROOT != FINAL_ROOT:
        if BASE_ROOT>FINAL_ROOT:SN[BASE_ROOT] = FINAL_ROOT
        else: SN[FINAL_ROOT] = BASE_ROOT
        ANS +=WEIGHT
print(ANS)

