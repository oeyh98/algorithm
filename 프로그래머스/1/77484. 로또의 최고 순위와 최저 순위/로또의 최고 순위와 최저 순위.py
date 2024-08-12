def solution(lottos, win_nums):
    answer = []
    rank = [6, 5, 4, 3, 2, 1, 6]
    correct = 0
    zero = 0
    for lotto in lottos:
        if lotto in win_nums:
            correct += 1
        elif lotto == 0:
            zero += 1
    
    answer.append(rank[correct + zero - 1])    
    answer.append(rank[correct - 1])
    
    return answer