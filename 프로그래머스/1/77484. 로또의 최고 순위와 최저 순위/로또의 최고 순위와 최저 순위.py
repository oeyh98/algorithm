def solution(lottos, win_nums):
    answer = []
    rank = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    correct = 0
    zero = 0
    
    for lotto in lottos:
        if lotto in win_nums:
            correct += 1
        elif lotto == 0:
            zero += 1
    
    answer.append(rank[correct + zero])    
    answer.append(rank[correct])
    
    return answer