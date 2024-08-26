from collections import deque
def solution(numbers, hand):
    answer = ""
    dial = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
    dial_map = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
        0: (3, 1), '*': (3, 0), '#': (3, 2)  
    }
    
    left = dial_map['*']
    right = dial_map['#']

    
    def bfs(start, target):
        queue = deque([start])
        visited = set()
        visited.add(start)
        distance = 0
        
        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                if (x, y) == target:
                    return distance
                
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:  
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < 4 and 0 <= ny < 3 and (nx, ny) not in visited:
                        if dial[nx][ny] != -1:  
                            visited.add((nx, ny))
                            queue.append((nx, ny))
            distance += 1
        return float('inf')
            
            
    
    for i in range(len(numbers)):
        if numbers[i] in [1, 4, 7, '*']:
            answer += "L"
            left = dial_map[numbers[i]]
        elif numbers[i] in [3, 6, 9, '#']:
            answer += "R"
            right = dial_map[numbers[i]]
        else:
            left_far = bfs(left, dial_map[numbers[i]])
            right_far = bfs(right, dial_map[numbers[i]])
            
            if left_far == right_far:
                if hand == "left":
                    answer += "L"
                    left = dial_map[numbers[i]]
                elif hand == "right":
                    answer += "R"
                    right = dial_map[numbers[i]]
                    
            elif left_far < right_far:
                answer += "L"
                left = dial_map[numbers[i]]
                
            else:
                answer += "R"
                right = dial_map[numbers[i]]

    return answer