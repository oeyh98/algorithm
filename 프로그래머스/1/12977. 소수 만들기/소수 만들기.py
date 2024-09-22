from itertools import combinations

def solution(nums):
    answer = 0
    
    def check(num):
        for i in range(2, num//2):
            if num % i == 0:
                return False
        return True
    
    for three in combinations(nums, 3):
        if check(sum(three)):
            answer += 1
            


    return answer