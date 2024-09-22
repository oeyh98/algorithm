def solution(n):
    cost = 0 
    while 0 < n:
        if n % 2 == 0:
            n //= 2
        
        else:
            n -= 1
            cost += 1
            
    return cost