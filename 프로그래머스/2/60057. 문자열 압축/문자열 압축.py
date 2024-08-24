def solution(s):    
    answer = len(s)

    for i in range(1, len(s)//2 + 1):
        comp_s = ""
        temp = s[:i]
        cnt = 1
        
        for j in range(i, len(s), i):
            if temp == s[j:j+i]:
                cnt += 1
            else:
                if 1 < cnt:
                    comp_s += str(cnt)
                    cnt = 1
                
                comp_s += temp    
                temp = s[j:j+i]
                
        if 1 < cnt:
            comp_s += str(cnt)
        comp_s += temp
        
        answer = min(answer, len(comp_s)) 
        
    return answer