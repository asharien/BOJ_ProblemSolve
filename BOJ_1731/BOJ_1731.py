import sys
BOX = []
for _ in range(int(sys.stdin.readline())):
    BOX.append(int(sys.stdin.readline()))
if(BOX[1]-BOX[0] == BOX[2]-BOX[1]):
    GAP = BOX[1]-BOX[0]
    print(BOX[-1]+GAP)
elif(BOX[1]//BOX[0] == BOX[2]//BOX[1]):
    GAP = BOX[1]//BOX[0]
    print(BOX[-1]*GAP)
