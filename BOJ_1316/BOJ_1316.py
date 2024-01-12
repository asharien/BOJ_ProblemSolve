import sys
N = int(sys.stdin.readline())
COUNT, BREAK_FLAG = 0, 0
REPEAT = []
for _ in range(N):
    TEMP = list(sys.stdin.readline().rstrip())
    for i in TEMP:
        if i in REPEAT:
            if i != MEMORY:
                BREAK_FLAG = 1
                break
        else:
            REPEAT.append(i)
            MEMORY = i

    if(BREAK_FLAG == 0):
        COUNT += 1
    else:
        BREAK_FLAG = 0
    REPEAT.clear()
    MEMORY = 0

print(COUNT)
