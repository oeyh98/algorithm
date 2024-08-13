def solution(s):
    answer = 0
    start = ''
    start_tmp = 0
    diff_tmp = 0
    
    for i in range(len(s)):    
        if start == '':
            start = s[i]
            start_tmp += 1
        else:
            if start == s[i]:
                start_tmp += 1
                
            else:
                diff_tmp += 1
                if start_tmp == diff_tmp:
                    answer += 1
                    start_tmp = 0
                    diff_tmp = 0
                    start = ''
        
    if start != '':
        answer += 1
        
    return answer