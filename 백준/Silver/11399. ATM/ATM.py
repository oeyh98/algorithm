n = int(input())
p = list(map(int, input().split()))

p.sort()
wait = 0
result = 0
for i in range(n):
    wait = wait + p[i]
    result += wait

print(result)