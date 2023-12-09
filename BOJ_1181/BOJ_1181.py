import sys
N = int(sys.stdin.readline())
WORDS = []
LINE_CHECKER = []
BOOK = []
for i in range(N):
    TEMP = str(sys.stdin.readline().rstrip())
    WORDS.append(TEMP)
WORDS = set(WORDS)
WORDS = list(WORDS)
LENGTH = len(WORDS)
for i in range(LENGTH):
    LINE_CHECKER.append(len(WORDS[i]))
for i in range(LENGTH):
    BOOK.append([LINE_CHECKER[i], WORDS[i]])

BOOK.sort(key = lambda x:(x[0], x[1]))
for i in range(LENGTH):
    print(BOOK[i][1])
