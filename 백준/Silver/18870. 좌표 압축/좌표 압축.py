n = int(input())

arr = list(map(int, input().split()))
dic = {}
new_arr = list(set(arr))
new_arr.sort()

for i, num in enumerate(new_arr):
    dic[num] = i

for j in arr:
    print(dic[j], end=' ')




