import sys
import collections
N = int(sys.stdin.readline())
BOX = []
for i in range(N):
    BOX.append(int(sys.stdin.readline()))
BOX.sort()
print(int(round(sum(BOX)/N)))
if(N%2 == 0):
    print((BOX[N//2]+BOX[(N//2)-1])/2)
else:
    print(BOX[N//2])
FREQUENCY = collections.Counter(BOX)
FREQUENCY = FREQUENCY.most_common(2)
if(N >=2):
    if(FREQUENCY[0][1] != FREQUENCY[1][1]):
        print(FREQUENCY[0][0])
    else:
        print(FREQUENCY[1][0])
else:
    print(FREQUENCY[0][0])

print(max(BOX)-min(BOX))
