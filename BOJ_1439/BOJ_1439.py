import sys
S = str(sys.stdin.readline().rstrip())
print(min(len(list(filter(bool, S.split("0")))), len(list(filter(bool, S.split("1"))))))
