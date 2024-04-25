import heapq
import sys

n = int(sys.stdin.readline())
queue = []

for _ in range(n):
    x = int(sys.stdin.readline())

    if x == 0:
        if len(queue) == 0:
            print("0")
        else:
            print(heapq.heappop(queue))
    else:
        heapq.heappush(queue, x)