import heapq
from collections import defaultdict

def dfs(cur, dic, path):
    
    while dic[cur]:
        next = heapq.heappop(dic[cur])
        dfs(next, dic, path)
    
    path.append(cur)

def solution(tickets):
    dic = defaultdict(list)
    
    for origin, dest in tickets:
        heapq.heappush(dic[origin], dest)

    path = []
    dfs("ICN", dic, path)
    return path[::-1]