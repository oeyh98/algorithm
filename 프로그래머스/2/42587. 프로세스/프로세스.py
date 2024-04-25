from collections import deque
def solution(priorities, location):
    answer = 0
    
    queue = deque([[i, p] for i, p in enumerate(priorities)])
    
    while queue:
        idx, current_process = queue.popleft()
        
        if any(current_process < roop_process for roop_idx, roop_process in queue):
            queue.append([idx, current_process])
        else:
            answer += 1
            if idx == location:
                return answer
            