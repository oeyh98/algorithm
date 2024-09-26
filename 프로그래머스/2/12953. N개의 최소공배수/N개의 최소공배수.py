def cal(temp, arr):
    for i in arr:
        if temp % i != 0:
            return False
    return True
                
                
def solution(arr):
    arr.sort()
    
    max_value = 1
    
    for i in arr:
        max_value *= i
    
    for temp in range(arr[-1], max_value + 1, arr[-1]):
        if cal(temp, arr):
            return temp

