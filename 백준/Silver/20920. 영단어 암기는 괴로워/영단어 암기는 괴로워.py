import sys
input = sys.stdin.readline
n, m = map(int, input().split())
words = {}

for _ in range(n):
    word = input().rstrip()
    if len(word) >= m:
        if word not in words:
            words[word] = 1
        else:
            words[word] += 1


sorted_words = sorted(words.keys(), key=lambda x:(-words[x], -len(x), x))

print(*sorted_words, sep='\n')