from sys import stdin
N, M = map(int, stdin.readline().split())
BOARD = [ ]
PLATE_SWITCHING = [ ]
COUNTER = 0
BOARD_CASE_A = [['BWBWBWBW'], ['WBWBWBWB'], ['BWBWBWBW'], ['WBWBWBWB'], ['BWBWBWBW'], ['WBWBWBWB'], ['BWBWBWBW'], ['WBWBWBWB']]
BOARD_CASE_B = [['WBWBWBWB'], ['BWBWBWBW'], ['WBWBWBWB'], ['BWBWBWBW'], ['WBWBWBWB'], ['BWBWBWBW'], ['WBWBWBWB'], ['BWBWBWBW']]
for i in range(N):
    BOARD.append(stdin.readline().split())

BOARD = list(BOARD)
for i in range(N):
    BOARD[i][0] = list(BOARD[i][0])

for i in range(8):
    BOARD_CASE_A[i][0] = list(BOARD_CASE_A[i][0])
    BOARD_CASE_B[i][0] = list(BOARD_CASE_B[i][0])

for i in range(N-7):
    for j in range(M-7):
        COUNTER = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if(BOARD[k][0][l] != BOARD_CASE_A[k-i][0][l-j]):
                    COUNTER = COUNTER + 1
                else:
                    continue
        PLATE_SWITCHING.append(COUNTER)
        COUNTER = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if(BOARD[k][0][l] != BOARD_CASE_B[k-i][0][l-j]):
                    COUNTER = COUNTER + 1
                else:
                    continue
        PLATE_SWITCHING.append(COUNTER)

print(min(PLATE_SWITCHING))
