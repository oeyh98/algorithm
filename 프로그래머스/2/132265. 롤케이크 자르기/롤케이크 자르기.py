def solution(topping):
    answer = 0
    old_dic = {}
    young_set = set()
    
    for i in range(len(topping)):
        if topping[i] not in old_dic:
            old_dic[topping[i]] = 1
        else:
            old_dic[topping[i]] += 1
    
    for t in topping:
        old_dic[t] -= 1
        young_set.add(t)
        
        if old_dic[t] == 0: old_dic.pop(t)
        
        if len(old_dic) == len(young_set):
            answer += 1
    
    return answer