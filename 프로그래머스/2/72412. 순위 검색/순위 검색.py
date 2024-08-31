from collections import defaultdict
from itertools import combinations
from bisect import bisect_left

def solution(info, query):
    answer = []
    info_dic = defaultdict(list)
    
    for i in range(len(info)):
        temp = info[i].split(" ")
        condition, score = temp[:-1], int(temp[-1])
        
        for j in range(5):
            for k in combinations(range(4), j):
                temp = condition.copy()
                
                for idx in k:
                    temp[idx] = '-'
                
                info_dic["".join(temp)].append(score)
    
    for values in info_dic.values():
        values.sort()
        
    for q in query:
        q = q.replace(" and ", "").split(" ")
        target, target_score = q[0], int(q[1])
        
        cnt = 0
        if target in info_dic:
            temp = info_dic[target]
            idx = bisect_left(temp, target_score)
            cnt += (len(temp) - idx)
        
        answer.append(cnt)
        
    return answer