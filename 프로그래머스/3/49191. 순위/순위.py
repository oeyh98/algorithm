from collections import defaultdict
def solution(n, results):
    answer = 0
    victory = defaultdict(set)
    defeat = defaultdict(set)
    
    for win, lose in results:
        victory[win].add(lose)
        defeat[lose].add(win)
        
    for i in range(1, n+1):
        for loser in victory[i]:
            defeat[loser].update(defeat[i])
        for winner in defeat[i]:
            victory[winner].update(victory[i])
            
    for i in range(1, n+1):
        if len(victory[i] | defeat[i]) == n - 1:
            answer += 1
            
    return answer