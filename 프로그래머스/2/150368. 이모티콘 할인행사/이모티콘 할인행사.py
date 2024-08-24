def solution(users, emoticons):
    answer = [0, 0]
    discount = []
    
    def bt(depth, temp):
        if depth == len(temp):
            discount.append(temp[:])
            return
            
        for per in [10, 20, 30, 40]:
            temp[depth] += per
            bt(depth + 1, temp)
            temp[depth] -= per
            
    bt(0, [0] * len(emoticons))
    
    for d in range(len(discount)):
        membership = 0
        profit = 0
        for u in range(len(users)):
            cost = 0
            for e in range(len(emoticons)):
                if users[u][0] <= discount[d][e]:
                    cost += int(emoticons[e] / 100) * (100 - discount[d][e])
                if users[u][1] <= cost:
                    membership += 1
                    cost = 0
                    break
                    
            profit += cost
        
        if answer[0] < membership:
            answer[0] = membership
            answer[1] = profit
        elif answer[0] == membership:
            answer[1] = max(answer[1], profit)
            
    return answer