import heapq
def solution(operations):
    q = []
    rq = []
    for op in operations:
        command, number = op.split()
        number = int(number)
        if command == 'I':
            heapq.heappush(q, number)
            heapq.heappush(rq, -number)
        elif command == 'D':
            if number == 1 and q:
                popped = heapq.heappop(rq)
                q.remove(-popped)
            elif number == -1 and q:
                popped = heapq.heappop(q)
                rq.remove(-popped)

    if not q:
        return [0,0]
    else:
        return [max(q), min(q)]