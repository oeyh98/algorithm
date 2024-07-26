def solution(book_time):
    stack = []
    
    def convert(time):
        h, m = map(int, time.split(":"))
        return h * 60 + m
    
    convert_time = sorted([(convert(st), convert(et) + 10) for st, et in book_time])
    
    for time in convert_time:
        if not stack:
            stack.append(time)
            continue
        
        for idx, reserved_time in enumerate(stack):
            if time[0] >= reserved_time[-1]:
                stack[idx] = reserved_time + time
                break
        else:
            stack.append(time)    
        
    return len(stack)