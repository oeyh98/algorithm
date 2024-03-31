def solution(s):
    answer = ''
    word = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    for i in range(len(word)):
        s = s.replace(word[i], str(i))
    
    
    return int(s)