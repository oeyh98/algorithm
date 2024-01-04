n = input()
arr = [int(i) for i in n]
arr.sort(reverse=True)

print(*arr, sep='')