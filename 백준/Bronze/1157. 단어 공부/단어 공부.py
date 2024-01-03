word = input().upper()

dic = {}
cnt = 0 
result = 1
for w in word:
    if w not in dic:
        dic[w] = 1
    else:
        dic[w] += 1
        
max_count = max(dic.values())

max_letters = [key for key, value in dic.items() if value == max_count]

print(max_letters[0] if len(max_letters) == 1 else '?')

