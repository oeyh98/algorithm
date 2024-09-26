def solution(gems):
    jewel_cnt = len(set(gems))
    answer = [1, len(gems)]
    min_len = float('inf')
    
    left = 0
    cur_cnt = {}
    
    
    for right in range(len(gems)):
        if gems[right] in cur_cnt:
            cur_cnt[gems[right]] += 1
        else:
            cur_cnt[gems[right]] = 1
            
            
        while len(cur_cnt) == jewel_cnt:
            if right - left < min_len:
                min_len = right - left
                answer = [left+1, right+1]
                
            cur_cnt[gems[left]] -= 1
            if cur_cnt[gems[left]] == 0:
                del cur_cnt[gems[left]]
                
            left += 1
            
    return answer