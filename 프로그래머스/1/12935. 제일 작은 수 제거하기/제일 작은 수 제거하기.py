def solution(arr):
    min_value = min(arr)
    arr = [x for x in arr if x != min_value]
    
    if not arr:
        return [-1]
        
    return arr