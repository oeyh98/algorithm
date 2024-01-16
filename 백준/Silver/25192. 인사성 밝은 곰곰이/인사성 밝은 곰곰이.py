n = int(input())
dic = {}
cnt = 0

for _ in range(n):
    gom = input()
    if gom == "ENTER":
        dic = {}
    else:
        if gom not in dic:
            dic[gom] = gom
            cnt += 1
        else:
            pass

print(cnt)