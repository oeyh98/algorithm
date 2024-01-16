m = int(input())
a = list(map(int, input().split()))
n = max(a)+1

a.sort()

print(a[0]*a[-1])