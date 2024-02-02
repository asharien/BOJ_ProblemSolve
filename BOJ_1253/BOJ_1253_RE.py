import sys
def main():
    N = int(sys.stdin.readline())
    L = list(sorted(map(int, sys.stdin.readline().split())))
    A = 0
    for i in range(len(L)):
        TARGET = L[i]
        TMP = L.copy()
        del TMP[i]
        UP, DW = 0, len(TMP)-1
        while UP<DW:
            S = TMP[UP] + TMP[DW]
            if S<TARGET: UP += 1
            elif S>TARGET: DW -= 1
            else:
                A += 1
                UP += 1
                DW -= 1
                break
    print(A)
if __name__ == "__main__":
    main()


