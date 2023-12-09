import sys
COMMAND = [ ]
SUB = [ ]
COMPARE = [ ]
N = int(sys.stdin.readline())
for i in range(N):
    COMMAND.append(sys.stdin.readline().strip())
PROMPT_LENGTH = len(COMMAND[0])
COMPARE = COMMAND[0]
COMPARE = list(COMPARE)
for i in range(N):
    SUB = list(COMMAND[i])
    for j in range(PROMPT_LENGTH):
        if(COMPARE[j] == SUB[j]):
            continue
        else:
            COMPARE[j] = '?'
print(*COMPARE, sep='')
