def solution(n, lost, reserve):
    dic = {i: 1 for i in range(1, n + 1)}
    answer = 0

    for l in lost:
        dic[l] -= 1

    for r in reserve:
        dic[r] += 1

    for idx in range(1, n + 1):
        if dic[idx] == 0:
            if idx - 1 > 0 and dic[idx - 1] > 1:
                dic[idx - 1] -= 1
                answer += 1
            elif idx < n and dic[idx + 1] > 1:
                dic[idx + 1] -= 1
                answer += 1
        else:
            answer += 1

    return answer
