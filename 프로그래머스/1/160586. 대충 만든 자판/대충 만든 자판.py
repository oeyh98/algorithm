def solution(keymap, targets):
    answer = []
    dic = {chr(i):100001 for i in range(65, 91)}
    
    for key in keymap:
        for idx, char in enumerate(key):
            if idx < dic[char]:
                dic[char] = idx + 1
                
    for target in targets:
        temp = 0
        for char in target:
            temp += dic[char] 
            
        answer.append(temp if temp < 10001 else -1)
        
    return answer
    
            