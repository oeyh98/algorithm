n, m = map(int, input().split())
arr = []
cnt = 0
dic = {}

for i in range(n):
    st = input().rstrip()
    dic[st] = 0

for _ in range(m):
    st = input().rstrip()
    if st in dic:
        cnt += 1

print(cnt)