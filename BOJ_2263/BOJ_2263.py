import sys
sys.setrecursionlimit(1000000)
def RETRACK(INS, INE, POSTS, POSTE):
    if (INS > INE) or (POSTS > POSTE): return
    ROOTINDEX = POSTORDER[POSTE]
    LEFT = BOOK[ROOTINDEX] - INS
    RIGHT = INE - BOOK[ROOTINDEX]
    ANS.append(ROOTINDEX)
    RETRACK(INS, INS+LEFT-1, POSTS, POSTS+LEFT-1)
    RETRACK(INE-RIGHT+1, INE, POSTE-RIGHT, POSTE-1)
BOOK, ANS = {}, []
N = int(sys.stdin.readline())
INORDER = list(map(int, sys.stdin.readline().split()))
POSTORDER = list(map(int, sys.stdin.readline().split()))
for i in range(N): BOOK[INORDER[i]] = i
RETRACK(0, N-1, 0, N-1)
print(*ANS)
