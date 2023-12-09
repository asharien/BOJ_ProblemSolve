import sys
for i in range(3):
    TMP = 0
    for _ in range(int(sys.stdin.readline())):
        TMP += int(sys.stdin.readline())
    if(TMP == 0): print('0')
    elif(TMP>0): print('+')
    else: print('-')
