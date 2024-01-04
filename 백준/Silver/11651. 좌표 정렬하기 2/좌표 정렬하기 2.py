import sys

n = int(sys.stdin.readline())

point = []
for i in range(n):
    point.append(list(map(int, sys.stdin.readline().split())))

point.sort(key=lambda x: (x[1], x[0]))
for p in point:
    print(p[0], p[1])