n = int(input())
result = []
items = []
for i in range(n):
    q, p = map(int, input().split())
    items.append([q, p])

items.sort(key=lambda s: (-s[0], s[1]))
print(items[0][0], items[0][1], items[1][0], items[1][1])
items.sort(key=lambda s: (s[1], -s[0]))
print(items[0][0], items[0][1], items[1][0], items[1][1])