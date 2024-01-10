def Bubblesort(lst):
    cnt = 0
    for i in range(len(lst)-1):
        for j in range(i, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
                cnt += 1

    return cnt

T = int(input())

for _ in range(T):
    n, *lst = map(int, input().split())
    print(n, Bubblesort(lst))

