a, b, v = map(int, input().split())
n = (v-b)//(a-b)
print (n if (v-b) % (a-b) == 0 else n + 1)