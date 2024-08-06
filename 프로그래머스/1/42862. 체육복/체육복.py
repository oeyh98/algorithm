def solution(n, lost, reserve):
    dic = {i:1 for i in range(n+1)}
    answer = 0
    
    for l in lost:
        dic[l] -= 1
        
    for r in reserve:
        dic[r] += 1
        
    for idx in dic:
        if dic[idx] == 0:
            if dic[idx-1] > 1:
                dic[idx-1] -= 1
                answer += 1
                
            elif idx + 1 < n + 1 and dic[idx + 1] > 1:
                dic[idx + 1] -= 1
                answer += 1
                
        else:
            answer += 1
            
    return answer - 1
                
                
    