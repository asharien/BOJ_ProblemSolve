import os
import shutil
import math

N = int(input())
SCORE = []
SCORE = input().split( )
SCORE = [eval(i) for i in SCORE]
FSCORE = []
FAKE = max(SCORE)
for i in SCORE:
    FSCORE.append(i/FAKE*100)


print(sum(FSCORE)/len(FSCORE))
