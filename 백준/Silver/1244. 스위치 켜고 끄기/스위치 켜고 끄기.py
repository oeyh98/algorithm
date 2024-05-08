switch_len = int(input())
switch = (list(map(int, input().split())))
student = int(input())

for s in range(student):
    gender, number = map(int, input().split())

    if gender == 1:
        i = 1
        while number * i <= switch_len:
            n = (number * i) - 1
            switch[n] = 0 if switch[n] == 1 else 1
            i += 1

    elif gender == 2:
        i = 1
        switch[number - 1] = 0 if switch[number - 1] == 1 else 1
        while 0 <= (number - i - 1) and (number + i - 1) < switch_len and switch[number - i - 1] == switch[number + i -1]:
            n = number + i - 1
            switch[n] = 0 if switch[n] == 1 else 1
            n = number - i - 1
            switch[n] = 0 if switch[n] == 1 else 1
            i += 1

if len(switch) <= 20:
    print(*switch)
else:
    for i in range(0, len(switch), 20):
        print(*switch[i:i+20])
