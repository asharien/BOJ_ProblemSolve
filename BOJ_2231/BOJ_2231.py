import sys
DIGIT_NUM = []
RUN = 0
def GET_NUM(DIGIT: int):
    while(DIGIT>0):
        DIGIT_NUM.append(DIGIT%10)
        DIGIT = DIGIT//10

    return sum(DIGIT_NUM)
N = int(sys.stdin.readline())
if(N>1000):
    RUN = int(N*0.9)
if(N<10):
    if(N%2 == 0): print(int(N/2))
    else: print("0")
else:
    while(1):
        RUN += 1
        SUB = GET_NUM(RUN)
        ANS = SUB+RUN
        if(ANS == N):
            print(RUN)
            break
        elif(ANS > N+ 100):
            print("0")
            break
        else:
            DIGIT_NUM.clear()
