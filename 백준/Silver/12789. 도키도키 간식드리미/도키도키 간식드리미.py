n = int(input())
line = list(map(int, input().split()))
stack = []
turn = 1
result = []

while line:
    if turn == line[0]:
        turn += 1
        result.append(line.pop(0))
    else:
        if stack and stack[-1] == turn:
            s = stack.pop()
            result.append(s)
            turn += 1
        else:
            stack.append(line.pop(0))

while stack:
    if stack[-1] != turn:
        break
    else:
        s = stack.pop()
        result.append(s)
        turn += 1

print('Sad' if stack else 'Nice')


