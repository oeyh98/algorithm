import heapq
import sys
input = sys.stdin.readline
n = int(input())
q = []

for _ in range(n):
    x = int(input())
    if x == 0:
        print(heapq.heappop(q)[1] if not len(q) == 0 else 0)
    else:
        heapq.heappush(q, (abs(x), x))
