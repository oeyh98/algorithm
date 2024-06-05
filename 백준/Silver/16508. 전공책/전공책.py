def get_char_frequency(s):
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq


def can_form_target(target_freq, books_freq):
    for char, count in target_freq.items():
        total_count = sum(book_freq.get(char, 0) for book_freq in books_freq)
        if total_count < count:
            return False
    return True


def find_min_cost(books, target_freq, index=0, current_books=None, min_cost=[float('inf')]):
    if current_books is None:
        current_books = []

    if index == len(books):
        if can_form_target(target_freq, [get_char_frequency(title) for _, title in current_books]):
            cost = sum(price for price, _ in current_books)
            min_cost[0] = min(min_cost[0], cost)
    else:
        find_min_cost(books, target_freq, index + 1, current_books + [books[index]], min_cost)
        find_min_cost(books, target_freq, index + 1, current_books, min_cost)

    return min_cost[0]


t = input().strip()
n = int(input())
books = []

for _ in range(n):
    parts = input().strip().split()
    price = int(parts[0])
    title = ''.join(parts[1:])
    books.append((price, title))

t_freq = get_char_frequency(t)

min_cost = find_min_cost(books, t_freq)
if min_cost == float('inf'):
    print(-1)
else:
    print(min_cost)
