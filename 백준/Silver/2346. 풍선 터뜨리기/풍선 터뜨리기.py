from collections import deque
n = int(input())
paper = list(map(int, input().split()))
dq = deque((i+1, paper[i]) for i in range(n))

while dq:
    idx, order = dq.popleft()
    print(idx, end= ' ')

    if order > 0:
        dq.rotate(-(order-1))
    else:
        dq.rotate(-(order))



