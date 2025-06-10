from collections import deque
def solution(begin, target, words):
    answer = 1e7
    n = len(words)
    visited = {}
    
    for word in words:
        visited[word] = False
    
    def dfs(cur, depth):
        nonlocal answer
        
        diff_one = set()
        
        if cur == target:
            answer = min(answer, depth)
            return
        
        for word in words:
            if not visited[word]:
                diff = 0
                for i in range(len(word)):
                    if word[i] != cur[i]:
                        diff += 1
                        
                        if 1 < diff: break
                        
                    
                if diff == 1:
                    diff_one.add(word)


        for word in diff_one:
            visited[word] = True
            dfs(word, depth+1)
            visited[word] = False
            
    
    dfs(begin, 0)
    return 0 if answer == 1e7 else answer