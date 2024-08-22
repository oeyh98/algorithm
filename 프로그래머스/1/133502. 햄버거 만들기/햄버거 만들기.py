def solution(ingredient):
    stack = []
    answer = 0
    for i in ingredient:
        stack.append(i)
        if stack[-4:] == [1, 2, 3, 1]:
            del stack[-4:]
            answer += 1
        
    return answer