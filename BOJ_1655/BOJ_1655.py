import sys
import heapq as HQ
H, L = [], []
for _ in range(int(sys.stdin.readline())):
    N = int(sys.stdin.readline())
    if len(H) == len(L): HQ.heappush(H, -N)
    else: HQ.heappush(L, N)
    if L and L[0] < -H[0]:
        T1, T2 = HQ.heappop(H), HQ.heappop(L)
        HQ.heappush(L, -T1)
        HQ.heappush(H, -T2)
    print(-H[0])
