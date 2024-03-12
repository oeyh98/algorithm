n = int(input())
arr = []
cnt = 0
for _ in range(n):
    start, end = map(int, input().split())
    arr.append([start, end])

arr.sort(key = lambda x:(x[1],x[0]))

start, end = 0, 0
for new_start, new_end in arr:
    if new_start >= end:
        cnt += 1
        end = new_end
        
print(cnt)
