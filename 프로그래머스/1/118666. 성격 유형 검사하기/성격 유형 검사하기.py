from collections import defaultdict
def solution(survey, choices):
    answer = ""
    indicator = defaultdict(int)
    
    score = [0, 3, 2, 1, 0, 1, 2, 3]
    
    for i in range(len(survey)):
        if choices[i] <= 4:
            indicator[survey[i][0]] += score[choices[i]]
        else:
            indicator[survey[i][1]] += score[choices[i]]
    
    print(indicator)
    answer += "R" if indicator["R"] >= indicator["T"] else "T"
    answer += "C" if indicator["C"] >= indicator["F"] else "F"
    answer += "J" if indicator["J"] >= indicator["M"] else "M"
    answer += "A" if indicator["A"] >= indicator["N"] else "N"
        
    return answer
