import sys

n = int(sys.stdin.readline())
array = [int(sys.stdin.readline()) for i in range(n)]

mean = round(sum(array)/n)
median = sorted(array)[int((n-1)/2)]

mode_dic = {}
for i in range(n):
    if array[i] in mode_dic:
        mode_dic[array[i]] += 1
    else:
        mode_dic[array[i]] = 1

max_mode_dic = max(mode_dic.values())
mode_list = [k for k, v in mode_dic.items() if max_mode_dic == v]
mode = mode_list[0] if len(mode_list) == 1 else sorted(mode_list)[1]

print(mean)
print(median)
print(mode)
print(max(array)-min(array))
