import sys
C=0
for i in range(8):
    CB = (list(str(sys.stdin.readline().rstrip())))
    if(i%2 == 0):
        for j in range(8):
            if(CB[j] == 'F' and j%2 ==0): C+=1
    else:
        for j in range(8):
            if(CB[j] == 'F' and j%2 ==1): C+=1
print(C)
