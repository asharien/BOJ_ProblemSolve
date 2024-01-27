import sys
DWF = list(sorted([int(sys.stdin.readline()) for i in range(9)]))
X, FLAG, FDWF = sum(DWF), False, []
for i in range(9):
    for j in range(i+1, 9):
        if X - DWF[i] - DWF[j] == 100:
            FDWF.append(DWF[i])
            FDWF.append(DWF[j])
            FLAG = True
            break
    if FLAG:break
for i in FDWF:DWF.remove(i)
for i in DWF: print(i)
