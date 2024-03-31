def solution(k, tangerine):
    answer = 0
    dic = {}
    for t in tangerine:
        if t not in dic:
            dic[t] = 1
        else:
            dic[t] += 1
            
    dic = sorted(dic.items(), key = lambda x:x[1], reverse= True)
    
    for key, value in dic:
        k -= value
        answer += 1
        if k <= 0:
            break
    return answer