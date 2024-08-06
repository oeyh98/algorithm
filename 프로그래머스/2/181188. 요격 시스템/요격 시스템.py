def solution(targets):
    targets.sort(key = lambda x : (x[0], x[1]))
    
    answer, prev_end = 0, 0
    
    for target in targets:
        s, e = target[0], target[1]
        
        if prev_end <= s:
            answer += 1
            prev_end = e
        else:
            prev_end = min(e, prev_end)
        
    return answer