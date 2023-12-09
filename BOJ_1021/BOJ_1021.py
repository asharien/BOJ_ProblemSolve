import sys
from collections import deque
N, TRASH= map(int, sys.stdin.readline().split())
TARGET = deque(map(int, sys.stdin.readline().rstrip().split()))
DECK, COUNT, WEIGHT= deque( _+1 for _ in range(N)), 0, N
for i in TARGET:
    WEIGHT = DECK.index(i)
    while(True):
        if(i == DECK[0]): 
            DECK.popleft()
            N -= 1
            break
        elif(WEIGHT>N//2):
            DECK.rotate(1)
            COUNT += 1
        elif(WEIGHT<=N//2):
            DECK.rotate(-1)
            COUNT += 1
print(COUNT)
