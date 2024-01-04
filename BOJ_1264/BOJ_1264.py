import sys
VOWELS = ['a', 'e', 'i', 'o', 'u']
while(1):
    WORDS = sys.stdin.readline().lower()
    WORDS = list(WORDS)
    COUNT = 0
    if(WORDS[0] == "#"):
        quit()
    else:
        for i in VOWELS:
            for j in WORDS:
                if(i == j):
                    COUNT += 1
                else:
                    continue
        print(COUNT)
        WORDS.clear()
