def solution(s):
    answer = []
    l = len(s)
    
    if l < 2:
        return l
    
    for i in range(1, l//2+1):
        comp_s = ""
        temp = s[:i]
        cnt = 1
        for j in range(i, len(s), i):
            if temp == s[j:j+i]:
                cnt += 1
            else:
                if cnt > 1:
                    comp_s += str(cnt) + temp
                else:
                    comp_s += temp
                cnt = 1
                temp = s[j:j+i]
            
        if cnt > 1:
            comp_s += str(cnt) + temp
        else:
            comp_s += temp
            
        answer.append(len(comp_s))
    
    return min(answer)