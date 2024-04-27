n = int(input())
file = list(map(int, input().split()))
cluster = int(input())
result = 0
if n != 0:
    for i in range(n):
        if file[i] == 0 : continue

        if file[i] > cluster:
            if file[i] % cluster == 0:
             result += cluster * (file[i] // cluster)
            else:
                result += cluster * ((file[i] // cluster) + 1)
        else:
            result += cluster

print(result)
