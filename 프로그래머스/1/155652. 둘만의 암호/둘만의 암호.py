def solution(s, skip, index):
    answer = ''
    alphabet = [chr(i) for i in range(97, 123)]
    for r in skip:
        alphabet.remove(r)
        
    for i in s:
        locate = alphabet.index(i)
        idx = locate + int(index)
        while idx >= len(alphabet): 
            idx -= len(alphabet)
        answer += alphabet[idx]
        
    return answer