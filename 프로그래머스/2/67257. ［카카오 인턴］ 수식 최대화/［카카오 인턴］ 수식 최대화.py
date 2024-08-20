
from itertools import permutations

def solution(expression):
    operations = ['+', '-', '*']
    operations = list(permutations(operations, 3))
    answer = []
    
    for op in operations:
        a = op[0]  
        b = op[1]    
        temp_list = []

        for ex in expression.split(a):
            temp = [f"({i})" for i in ex.split(b)]
            temp_list.append(f'({b.join(temp)})')

        answer.append(abs(eval(a.join(temp_list))))
        
    return max(answer)  