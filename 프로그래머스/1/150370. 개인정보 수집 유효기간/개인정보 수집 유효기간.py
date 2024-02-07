def solution(today, terms, privacies):
    answer = []
    dic = {}
    y, m, d = map(int, today.split('.'))
    
    for t in terms:
        term, period = t.split()
        dic[term] = int(period)
    
    
    for i in range(len(privacies)):
        p_date, term = privacies[i].split()
        py, pm, pd = map(int, p_date.split('.'))
        
        for j in range(dic[term]):
            pd += 28
            
            if pd > 28:
                pd -= 28
                pm += 1
            
            if pm > 12:
                pm -= 12
                py += 1
        if py < y or (py == y and pm < m) or (py == y and pm == m and pd <= d):
            answer.append(i+1)
        
        print(py, pm, pd)
        
    return answer