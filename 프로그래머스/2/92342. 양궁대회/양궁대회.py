from itertools import combinations_with_replacement

def solution(n, info):
    answer = [-1]
    max_diff = 0
    
    for i in list(combinations_with_replacement(range(0,11),n)):
        lion_score = 0
        apeach_score = 0
        
        lion = [0] * 11
        
        for j in i:
            lion[j] += 1
    

        for k in range(0, 11):
            if info[k] < lion[k]:
                lion_score += (10-k)
            else:
                apeach_score += (10-k)
                
        if max_diff < lion_score - apeach_score:
            max_diff = lion_score - apeach_score
            answer = lion
            
    return answer