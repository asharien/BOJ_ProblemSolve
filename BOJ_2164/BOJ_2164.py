import sys
from collections import deque
CARD = [ ]
N = int(sys.stdin.readline())
for i in range(N):
    CARD.append(i+1)
CARD = deque(CARD)

while(len(CARD) != 1):
    CARD.popleft()
    TEMP = CARD.popleft()
    CARD.append(TEMP)


print(*CARD)
