def convert(time):
    y, m, d = map(int, time.split("."))
    return y * 12 * 28 + m * 28 + d

def solution(today, terms, privacies):
    answer = []
    term_dic = {}
    
    cur = convert(today)
    
    for term in terms:
        a, b = term.split(' ')
        term_dic[a] = int(b) * 28
    
    for i in range(len(privacies)):
        privacie, term = privacies[i].split(' ')
        nd = convert(privacie)
        
        if nd + term_dic[term] <= cur:
            answer.append(i+1)
            
    return answer


