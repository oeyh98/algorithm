def solution(survey, choices):
    answer = ''
    dic = {}
    indicator = ['R', 'T', 'C', 'F', 'J', 'M', 'A', 'N']
    score = [3, 2, 1, 0, 1, 2, 3]
    
    for i in indicator:
        dic[i] = 0
    
    for i in range(len(survey)):
        if choices[i] < 4:
            dic[survey[i][0]]  += score[choices[i]-1]
        else:
            dic[survey[i][1]]  += score[choices[i]-1]
            
    answer += 'T' if dic['R'] < dic['T'] else 'R'
    answer += 'F' if dic['C'] < dic['F'] else 'C'
    answer += 'M' if dic['J'] < dic['M'] else 'J'
    answer += 'N' if dic['A'] < dic['N'] else 'A'
    
    
    return answer