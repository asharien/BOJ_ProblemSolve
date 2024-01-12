import sys
RECORD = {}
for _ in range(int(sys.stdin.readline())):
    B = str(sys.stdin.readline().rstrip())
    try:RECORD[B] += 1
    except:RECORD[B] = 1
HOLDER = max(RECORD.values())
RECORD = sorted(RECORD.items(), key = lambda x:x[0])
for key, val in RECORD:
    if val == HOLDER:
        print(key)
        break
