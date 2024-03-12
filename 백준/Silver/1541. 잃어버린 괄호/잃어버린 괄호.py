minus_div = input().split('-')
nums = []

for s in minus_div:
    tmp = 0
    plus_div = s.split('+')

    for n in plus_div:
        tmp += int(n)

    nums.append(tmp)

result = nums[0]

for i in nums[1:]:
    result -= i

print(result)