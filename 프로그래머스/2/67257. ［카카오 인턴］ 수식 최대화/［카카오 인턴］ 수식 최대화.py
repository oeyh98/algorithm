from itertools import permutations
from collections import deque

def operation(left, right, op):
    left = int(left)
    right = int(right)
    
    if op == '+':
        return left + right
    elif op == '-':
        return left - right
    else: 
        return left * right

def calculator(ops, expression):
    q = deque()
    temp = ""
    
    for ex in expression:
        if ex.isdigit():
            temp += ex
        else:
            if temp:
                q.append(temp)
                temp = ""
            q.append(ex)
    
    if temp:
        q.append(temp)
    

    for op in ops:
        stack = []
        while q:
            ex = q.popleft()
            if ex == op:
                stack.append(operation(stack.pop(), q.popleft(), op))
            else:
                stack.append(ex)
        q = deque(stack)  # 스택을 다시 큐로 변환
    
    return abs(int(q[0]))  # 최종 결과 반환

def solution(expression):
    answer = []
    for ops in permutations(['+', '-', '*'], 3):
        answer.append(calculator(ops, expression))
        
    return max(answer)

# 테스트
print(solution("100-200*300-500+20"))  # 기대값: 60420
