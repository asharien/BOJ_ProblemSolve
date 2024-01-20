import sys
N = int(sys.stdin.readline())
START_LINE = 666
SCANNER = 0
while(1):
    MOVIE_NAME = str(START_LINE)
    if "666" in MOVIE_NAME:
        SCANNER += 1
        if(SCANNER == N):
            break
    START_LINE += 1

print(MOVIE_NAME)
