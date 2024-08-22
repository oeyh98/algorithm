from itertools import combinations
def solution(relation):
    answer = 0
    col = len(relation[0])
    row = len(relation)
    
    combis = []
    # 조합 생성
    for i in range(1, col + 1):
        combis.extend(combinations(range(col), i))

    # 유일성  
    unique = []
    answer = 0
    
    for comb in combis:
        tmp = [tuple(item[key] for key in comb) for item in relation]
        if len(set(tmp)) == row :
            flag = True
            
            for u in unique:
                if set(u).issubset(set(comb)):
                    flag = False
                    break
                
            if flag :
                unique.append(comb)
            
    
    return len(unique)