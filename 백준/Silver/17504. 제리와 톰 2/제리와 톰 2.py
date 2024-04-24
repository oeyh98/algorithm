n = int(input())
nums = list(map(int, input().split()))

idx = len(nums) - 1
a1, a2 = nums[idx], 1
idx -= 1

while idx >= 0:
    a2 = nums[idx] * a1 + a2
    idx -= 1
    a1, a2 = a2, a1

a2 = a1 - a2

print(a2, a1)

