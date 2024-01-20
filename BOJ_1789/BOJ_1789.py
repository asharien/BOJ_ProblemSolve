import sys
N = int(sys.stdin.readline())
COUNT, SUM = 0, 0
while(1):
    COUNT += 1
    SUM += COUNT
    if(SUM > N): break
print(COUNT-1)
