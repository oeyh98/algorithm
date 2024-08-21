def solution(X, Y):
    answer = ""
    set_XY = sorted(set(X) & set(Y), reverse = True)
    
    for i in set_XY:
        answer += i * min(X.count(i), Y.count(i))
    
    if answer == "":
        return "-1"
    elif len(answer) == answer.count('0'):
        return "0"
    else:
        return answer