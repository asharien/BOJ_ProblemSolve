import sys
def FACTORIAL(N):
    if(N == 0):
        return 1
    return N*FACTORIAL(N-1)
N = int(sys.stdin.readline())
COUNT = 0
ZEROS = str(FACTORIAL(N))
ZEROS = list(ZEROS)
for i in range(len(ZEROS), 0, -1):
    if(ZEROS[i-1] == '0'):
        COUNT += 1
    else:
        break
print(COUNT)
