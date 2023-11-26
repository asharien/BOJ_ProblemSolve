import sys
PATTERN = [[10], [1], [2,4,8,6], [3,9,7,1], [4,6], [5], [6], [7, 9, 3, 1], [8, 4, 2, 6], [9, 1]]
OUTPUT = []
CASE = int(sys.stdin.readline())
for i in range(CASE):
    TEMP, TEMP2 = map(int, sys.stdin.readline().split())
    A = TEMP%10
    B = TEMP2%len(PATTERN[A])
    OUTPUT.append(PATTERN[A][B-1])
for i in range(CASE): print(OUTPUT[i])
