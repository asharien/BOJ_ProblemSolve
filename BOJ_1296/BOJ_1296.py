import sys
from collections import Counter
LOVE = "LOVE"
N, ANS, SC = Counter(str(sys.stdin.readline().rstrip())), {}, 1
for _ in range(int(sys.stdin.readline())):
    TEAM = str(sys.stdin.readline().rstrip())
    TMP = Counter(TEAM)
    for i in range(4):
        for j in range(i, 4):
            A, B = LOVE[i], LOVE[j]
            if(i!=j): SC *= (N[A]+TMP[A]+N[B]+TMP[B])
    ANS[TEAM], SC = SC%100, 1
FINAL = sorted(ANS.items())
FINAL.sort(key=lambda x: (-x[1], x[0]))
print(FINAL[0][0])
