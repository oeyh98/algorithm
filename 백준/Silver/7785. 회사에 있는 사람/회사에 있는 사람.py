n = int(input())
dic = {}

for _ in range(n):
    log = input().split()

    if log[0] not in dic:
        dic[log[0]] = log[1]

    else:
        dic[log[0]] = log[1]

sorted_dic = sorted(dic.items(), reverse=True)

for key, value in sorted_dic:
    if value == "enter":
        print(key)
