import sys
INDEX, PLACEHOLDER, CHECK = {}, 0, 0
WORD = list(str(sys.stdin.readline().rstrip().upper()))
for i in WORD:
    try: INDEX[i] += 1
    except: INDEX[i] = 1
for key, val in INDEX.items():
    if(PLACEHOLDER < val): 
        PLACEHOLDER = val
        ANS = key
        CHECK = 0
    elif(PLACEHOLDER == val): CHECK = 1
print(ANS if CHECK != 1 else "?")

