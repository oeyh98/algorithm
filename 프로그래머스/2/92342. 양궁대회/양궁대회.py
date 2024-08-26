from itertools import combinations_with_replacement

def solution(n, info):
    answer = [-1]
    max_diff = 0
    
    for i in list(combinations_with_replacement(range(0,11), n)):
        lion_score = 0
        apeach_score = 0
        lion = [0] * 11
        
        for j in i:
            lion[j] += 1
    
        lion = lion[::-1]
        for k in range(0, 11):
            if info[k] < lion[k]:
                lion_score += (10-k)
            elif info[k]:
                apeach_score += (10-k)
                
        score_diff = lion_score - apeach_score
        if max_diff < score_diff:
            max_diff = score_diff
            answer = lion
            
    return answer
