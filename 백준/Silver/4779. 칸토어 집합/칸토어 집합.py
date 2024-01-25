def kan(n):
    if n == 1:
        return '-'

    l = n//3

    return kan(l) + ' '*l + kan(l)


while True:
    try:
        n = int(input())
        arr = kan(3**n)
        print(arr)
    except:
        break