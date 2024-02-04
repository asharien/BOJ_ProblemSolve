from sys import stdin as STD
NAME = []
AGE = []
WEIGHT = []
while(1):
    TEMP1, TEMP2, TEMP3 = STD.readline().split()
    if(TEMP1 == "#"):
        break
    NAME.append(str(TEMP1))
    AGE.append(int(TEMP2))
    WEIGHT.append(int(TEMP3))

for i in range(len(NAME)):
    if(AGE[i]>17 or WEIGHT[i] >= 80):
        print(NAME[i], "Senior")
    else:
        print(NAME[i], "Junior")
