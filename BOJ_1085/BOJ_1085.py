import sys
X, Y, W, H = map(int, (sys.stdin.readline().split()))
TO_BORDER_X = W-X
TO_BORDER_Y = H-Y
print(min(X, Y, TO_BORDER_X, TO_BORDER_Y))
