import sys
while(True):
    IN, CMD, OUT = map(str, sys.stdin.readline().rstrip().split())
    if [IN, CMD, OUT] == ['0', 'W', '0']:break
    IN, OUT = int(IN), int(OUT)
    if CMD == 'W': print(IN-OUT if IN-OUT>=-200 else "Not allowed")
    elif CMD == 'D':print(IN+OUT)

