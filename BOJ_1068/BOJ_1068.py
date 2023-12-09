import sys
from math import inf as INF
def REMOVE(TREE, DEL):
    TREE[DEL] = -INF
    for i in range(len(TREE)):
        if DEL == TREE[i]: REMOVE(TREE, i)

TRASH = int(sys.stdin.readline())
TREE = list(map(int, sys.stdin.readline().split()))
DEL = int(sys.stdin.readline())
REMOVE(TREE, DEL)
ANS = 0
for i in range(len(TREE)):
    if(TREE[i] != -INF and i not in TREE):
        ANS += 1
print(ANS)
