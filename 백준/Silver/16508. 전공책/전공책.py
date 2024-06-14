import sys
input = sys.stdin.readline

t = input().rstrip()
n = int(input())

cost = []
books = []

min_cost = 1e9

for _ in range(n):
    c, w = input().rstrip().split()
    cost.append(int(c))
    books.append(w)


def can_form_target(target, chosen_books):
    target_freq = {}
    for char in target:
        if char in target_freq:
            target_freq[char] += 1
        else:
            target_freq[char] = 1

    book_freq = {}
    for idx in chosen_books:
        for char in books[idx]:
            if char in book_freq:
                book_freq[char] += 1
            else:
                book_freq[char] = 1

    for char in target_freq:
        if char not in book_freq or book_freq[char] < target_freq[char]:
            return False

    return True


def dfs(depth, current_books):
    global min_cost

    if depth == n:
        if can_form_target(t, current_books):
            total = sum(cost[idx] for idx in current_books)
            min_cost = min(total, min_cost)

    else:
        dfs(depth + 1, current_books + [depth])
        dfs(depth + 1, current_books)


dfs(0, [])
print(min_cost if min_cost != 1e9 else -1)
