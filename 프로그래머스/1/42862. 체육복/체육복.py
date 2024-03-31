def solution(n, lost, reserve):
    lost_set = set(lost) - set(reserve)
    reserve_set = set(reserve) - set(lost)
    
    for item in reserve_set:
        if item - 1 in lost_set:
            lost_set.remove(item - 1)
            
        elif item + 1 in lost_set:
            lost_set.remove(item + 1)
            
        
    return n - len(lost_set)