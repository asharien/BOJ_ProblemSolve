import sys
for _ in range(int(sys.stdin.readline())):
    X = list(map(str, sys.stdin.readline().rstrip().split('-')))
    ALP =sum([(ord(X[0][i])-65)*(26**(2-i)) for i in range(3)])
    NUM = int(X[1])
    print("nice" if abs(ALP-NUM)<=100 else "not nice")
