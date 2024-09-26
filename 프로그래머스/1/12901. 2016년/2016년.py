def solution(a, b):
    week = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    temp = 0
    for i in range(a-1):
        temp += month[i]
        
    day = week[(b + temp -1) % 7]

    return day
