n, k = map(int, input().split())
arr = list(map(int, input().split()))
ans = []

def m_split(data):
    if len(data) <= 1:
        return data

    mid = (len(data)+1)//2

    left = m_split(data[:mid])
    right = m_split(data[mid:])

    return merge(left, right)

def merge(left, right):
    lst = []
    lp, rp = 0, 0

    while len(left) > lp and len(right) > rp:
        if left[lp] > right[rp]:
            lst.append(right[rp])
            ans.append(right[rp])
            rp+=1
        else:
            lst.append(left[lp])
            ans.append(left[lp])
            lp += 1
    while len(left) > lp :
        lst.append(left[lp])
        ans.append(left[lp])
        lp += 1
    while len(right) > rp :
        lst.append(right[rp])
        ans.append(right[rp])
        rp += 1
    return lst


m_split(arr)
if len(ans) >= k:
    print(ans[k-1])
else:
    print(-1)
