import sys
CND = [int(sys.stdin.readline()) for i in range(int(sys.stdin.readline()))]
print("S" if CND[0] == max(CND) else "N")
