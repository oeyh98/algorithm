import sys
input = sys.stdin.readline
n = int(input())

dic = {}
dic['ChongChong'] = 'ChongChong'

for _ in range(n):
    a, b = input().split()
    if a in dic:
        dic[b] = b
    elif b in dic:
        dic[a] = a
    else:
        continue


print(len(dic))