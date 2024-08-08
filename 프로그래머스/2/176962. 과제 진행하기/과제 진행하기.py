def convert(m):
    m = list(map(int, m.split(":")))
    return m[0] * 60 + m[1]

def solution(plans):
    answer = []
    stack = []
    
    for i in range(len(plans)):
        plans[i][1] = convert(plans[i][1])
        plans[i][2] = int(plans[i][2])
        
    plans.sort(key = lambda x : (x[1], x[2]))
    
    for i in range(len(plans) - 1):
        subject, start_time, play_time  = plans[i]
        remain = plans[i+1][1] - start_time
        
        if play_time <= remain:
            answer.append(subject)
            remain = remain - play_time
                
            while stack and remain:
                if stack[-1][1] <= remain:
                    stoped_subject, staoped_time = stack.pop()
                    answer.append(stoped_subject)
                    remain = remain - staoped_time
                else:
                    stack[-1][1] -= remain
                    remain = 0
            
        else:
            stack.append([subject, play_time - remain])
            
    answer.append(plans[-1][0])
    
    while stack:
        answer.append(stack.pop()[0])
            
    return answer