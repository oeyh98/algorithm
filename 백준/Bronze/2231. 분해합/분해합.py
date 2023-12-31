n = int(input())
result = 0

for i in range(1, n):
    split_sum = i + sum(map(int, str(i)))
    if split_sum == n:
        result = i
        break

print(result)