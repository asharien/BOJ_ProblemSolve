import sys
while(True):
    S = list(map(str, sys.stdin.readline().lower().rstrip().split()))
    CNT =0
    if(S[0] == '#'):break
    for i in S:
        if S[0] in i: CNT += i.count(S[0])
    print(S[0], CNT-1)
