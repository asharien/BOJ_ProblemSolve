import sys
A, B = map(int, sys.stdin.readline().split())
A = int(A)
B = int(B)
if(A>B):
    print(">")
elif(A<B):
    print("<")
elif(A==B):
    print("==")
else:
    print("Wrong")
    
    
