import heapq
def solution(n, k, enemy):
    answer = 0
    heap = []
    total = 0
    for e in enemy :
        heapq.heappush(heap, -e)
        total += e
        if total > n :
            if k == 0 :
                break
            k -= 1
            total += heapq.heappop(heap)
            
        else:
            n -= e
            total -= e
        
        answer += 1
    return answer