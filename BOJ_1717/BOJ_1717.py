import sys
N, M = map(int, sys.stdin.readline().split())
GROUP, CNT = {i:i for i in range(N+1)}, 0
def SEARCH(LOOKUP, TAG):
    while(LOOKUP[TAG] != TAG):
        TAG = LOOKUP[TAG]
    return TAG
def TIE(LOOKUP, EA, EB):
    SET_A = SEARCH(LOOKUP, EA)
    SET_B = SEARCH(LOOKUP, EB)
    if SET_A > SET_B: LOOKUP[SET_B] = SET_A
    else: LOOKUP[SET_A] = SET_B
for i in range(M):
    CMD, EA, EB = map(int, sys.stdin.readline().split())
    if(CMD == 0): TIE(GROUP, EA, EB)
    elif(CMD == 1):
        if SEARCH(GROUP, EA) == SEARCH(GROUP, EB): print("YES")
        else: print("NO")
