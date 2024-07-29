def solution(storey):
    answer = 0 
    
    while storey > 0:
        num_digits = len(str(storey))
        case_a = abs(storey - 10 ** num_digits)
        case_b = abs(storey - 10 ** (num_digits - 1))
        storey = min(case_a, case_b)

        answer += 1
        
    return answer
