def solution(arr):
    min_value = min(arr)
    arr.remove(min_value)
    
    if not arr:
        return [-1]
        
    return arr