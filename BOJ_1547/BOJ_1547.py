import sys
YABAWI = {1:1, 2:0, 3:0}
for _ in range(int(sys.stdin.readline())):
    N, M = map(int , sys.stdin.readline().split())
    TEMP = YABAWI[N]
    YABAWI[N] = YABAWI[M]
    YABAWI[M] = TEMP
for key, val in YABAWI.items():
    if(val ==1): print(key)
