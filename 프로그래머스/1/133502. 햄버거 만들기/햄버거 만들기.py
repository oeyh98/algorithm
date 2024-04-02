def solution(ingredient):
    answer = 0
    # stack = []
    # for i in range(len(ingredient)):
    #     stack.append(ingredient[i])
    #     if stack[-4:] == [1, 2, 3, 1]:
    #         stack = stack[:-4]
    #         answer += 1
    
    s = []
    cnt = 0
    for i in ingredient:
        s.append(i)
        if s[-4:] == [1, 2, 3, 1]:
            cnt += 1
            for _ in range(4):
                s.pop()
    return cnt
        
    return answer