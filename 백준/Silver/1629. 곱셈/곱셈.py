# A^m+n = A^m x A^n
# (AxB)%C = (A%C) *(B%C) % C
a, b, c = map(int, input().split(" "))
num = a


def multi(a, b, c):
    if b == 1:
        return a % c

    if b % 2 == 0:
        return (multi(a, b//2, c)**2) % c
    else:
        return ((multi(a, b//2, c)**2) *a) % c

print(multi(a, b, c))