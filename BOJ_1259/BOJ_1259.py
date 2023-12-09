from sys import stdin as STD
FLIP = []
WORDS = []
while(1):
    WORDS = str(STD.readline().rstrip())
    WORDS = list(WORDS)
    LENGTH = len(WORDS)
    if(LENGTH == 1):
        if(WORDS[0] == '0'):
            break
    FLIP = list(reversed(WORDS))
    if(WORDS == FLIP):
        print("yes")
    else:
        print("no")
        
