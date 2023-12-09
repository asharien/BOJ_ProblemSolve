import sys
SUM, COUNT, PASS_FLAG = 0, 0, 0
PATTERN = []
X = int(sys.stdin.readline())
if(X == 1):
    PASS_FLAG = 1
else:
    while(SUM<X):
        COUNT +=1
        SUM = SUM+COUNT
        MEMORIZE = COUNT
if(SUM-X != 0):
    NEXTO = SUM - X
else:
    NEXTO = 0
if(COUNT%2 == 0 and PASS_FLAG == 0):
    for i in range(COUNT):
        TEMP = str(i+1) + '/' + str(COUNT-i)
        PATTERN.append(TEMP)
elif(PASS_FLAG == 1):
    PATTERN.append('1/1')
else:
    for i in range(COUNT):
        TEMP = str(COUNT-i) + '/' + str(i+1)
        PATTERN.append(TEMP)
COUNT = COUNT - NEXTO -1
print(PATTERN[COUNT])
