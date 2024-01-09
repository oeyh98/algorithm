k = int(input())
stack = []

for i in range(k):
    order = int(input())
    if order == 0:
        stack.pop()
    else:
        stack.append(order)

print(sum(stack))