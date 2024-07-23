def solution(numbers):
    numbers = list(map(str, numbers))
    #자리 수를 맞춘 후, 사전 순 비교    
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))