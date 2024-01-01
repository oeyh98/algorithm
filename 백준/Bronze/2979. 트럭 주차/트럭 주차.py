import sys

fee_lst = [0] + list(map(int, sys.stdin.readline().split()))
at = list(map(int, sys.stdin.readline().split()))
bt = list(map(int, sys.stdin.readline().split()))
ct = list(map(int, sys.stdin.readline().split()))

cars = 0
fee = 0

first_in = min(at[0], bt[0], ct[0])
last_out = max(at[1], bt[1], ct[1])

for i in range(first_in, last_out +1):
    if i == at[0]:
        cars += 1
    if i == bt[0]:
        cars += 1
    if i == ct[0]:
        cars += 1

    if i == at[1]:
        cars -= 1
    if i == bt[1]:
        cars -= 1
    if i == ct[1]:
        cars -= 1

    fee += fee_lst[cars]*cars


print(fee)