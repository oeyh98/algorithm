def solution(n, arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        tmp = (bin(arr1[i]|arr2[i]))[2:]
        if len(tmp) < n:
            tmp = tmp.zfill(n)
        tmp = tmp.replace("1", "#").replace("0", " ")
        answer.append(tmp)
    return answer