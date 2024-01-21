def divisor(num):
    answer = []
    for i in range(1, num+1):
         if num%i == 0: 
            answer.append(i)    
    return answer

def solution(left, right):
    count = 0
    for i in range(left, right+1):
        count = count + i if len(divisor(i))%2 == 0 else count - i
    return count