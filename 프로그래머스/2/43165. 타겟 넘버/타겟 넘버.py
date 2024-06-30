def solution(numbers, target):
    return dfs(0, numbers, target, 0)

def dfs(depth, numbers, target, total):
    if depth == len(numbers):
        return 1 if total == target else 0
    
    plus = dfs(depth + 1 ,numbers, target, total + numbers[depth])
    minus = dfs(depth + 1 ,numbers, target, total + (numbers[depth] * (-1))) 
    
    return plus + minus
    
    