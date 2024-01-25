def solution(friends, gifts):
    table = {}
    score = {}
    result = {}
        
    for friend in friends:
        table[friend] = {f:0 for f in friends}
        score[friend] = 0
        result[friend] = 0
        
    for gift in gifts:
        giver, receiver = gift.split(' ')
        
        table[giver][receiver] += 1
        
        score[giver] += 1
        score[receiver] -= 1
    
    for i in range(len(friends)-1):
        for j in range(i, len(friends)):
            
            more_gift = table[friends[i]][friends[j]] - table[friends[j]][friends[i]]
            
            if more_gift > 0:
                result[friends[i]] += 1
            elif more_gift < 0:
                result[friends[j]] += 1
            else:
                if score[friends[i]] > score[friends[j]]:
                    result[friends[i]] += 1
                elif score[friends[i]] < score[friends[j]]:
                    result[friends[j]] += 1
    
    answer = result[max(result, key=result.get)]
    return answer