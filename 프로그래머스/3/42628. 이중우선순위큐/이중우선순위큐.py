from heapq import heappush, heappop
def solution(operations):
    hq = []
    rhq = []
    
    for operation in operations:
        cmd, data = operation.split(" ")
        data = int(data)
        
        if cmd == 'I':
            heappush(hq, data)
            heappush(rhq, -data)
        elif cmd == "D":
            if data == -1 and hq:
                temp = heappop(hq)
                rhq.remove(-temp)
            elif data == 1 and hq:
                temp = heappop(rhq)
                hq.remove(-temp)
         
    if hq:
        return [max(hq), min(hq)]
    else:
        return [0, 0]