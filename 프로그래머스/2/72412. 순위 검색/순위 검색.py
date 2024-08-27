from itertools import combinations
from collections import defaultdict

def bin_search(target, scores, start, end):
    while start <= end:
        mid = (start + end) // 2
        if scores[mid] >= target:
            end = mid - 1
        else:
            start = mid + 1
    return start

def solution(information, queries):
    answer = []
    dic = defaultdict(list)
    
    for info in information:
        info = info.split()
        condition = info[:-1]
        score = int(info[-1])
        
        for i in range(5):
            case = list(combinations(range(4), i))
            
            for c in case:
                temp = condition.copy()
                for idx in c:
                    temp[idx] = '-'
                key = ' '.join(temp)
                dic[key].append(score)
        
        
    for values in dic.values():
        values.sort()
        
    for query in queries:
        query = query.replace(' and', '')
        query = query.split()
        
        target_condition = ' '.join(query[:-1])
        target_score = int(query[-1])
        
        scores = dic[target_condition]
        scores_len = len(scores)
        cnt = bin_search(target_score, scores, 0, scores_len-1)
        result = scores_len - cnt
        answer.append(result)    
                    
    return answer