import sys
N = int(sys.stdin.readline())
HISTORY = {}
WATCHER = 0
ANS = []
for _ in range(N):
    TEMP = str(sys.stdin.readline().rstrip())
    if TEMP[0] not in HISTORY: HISTORY[TEMP[0]] = 1
    else: HISTORY[TEMP[0]] += 1
for key, value in HISTORY.items():
    if(value>=5):
        ANS.append(key)
    else:
        WATCHER += 1
ANS.sort()
if(WATCHER == len(HISTORY)):
    print("PREDAJA")
else:
    print(*ANS, sep="")
