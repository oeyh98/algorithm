from itertools import combinations

def solution(relation):
    row = len(relation)
    col = len(relation[0])
    
    comb = []
    
    for i in range(1, col + 1):
        for c in combinations(range(col), i):
            comb.append(c)
    
    unique = []
    for c in comb:
        temp = set()
        
        for r in relation:
            temp.add(tuple(r[idx] for idx in c))
            
        if len(temp) == row:
            flag = True
            
            for u in unique:
                if set(u).issubset(set(c)):
                    flag = False
                    break
            
            if flag:
                unique.append(c)

    return len(unique)