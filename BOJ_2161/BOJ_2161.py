import sys
from collections import deque
CASE = int(sys.stdin.readline())
DECK = deque(_ for _ in range(1, CASE+1))
ANS =deque()
while(len(DECK) != 0):
    TEMP = DECK.popleft()
    DECK.rotate(-1)
    ANS.append(TEMP)

print(*ANS)
