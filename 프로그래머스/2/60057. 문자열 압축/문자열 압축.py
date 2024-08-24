def solution(s):    
    answer = len(s)

    for i in range(1, len(s)//2 + 1):
        comp_s = ""
        cnt = 1
        
        for j in range(0, len(s), i):
            if s[j:j+i] == s[j+i:j+i*2]:
                cnt += 1
            else:
                if 1 < cnt:
                    comp_s += str(cnt)
                    
                cnt = 1
                comp_s += s[j:j+i]    
        
        answer = min(answer, len(comp_s)) 
        
    return answer

