def solution(arr):
    min_value = min(arr)
    arr = [x for x in arr if x != min_value] 

    return arr if arr else [-1]
