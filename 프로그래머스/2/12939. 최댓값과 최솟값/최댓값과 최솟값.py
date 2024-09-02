def solution(s):
    ss = list(map(int, s.split(" ")))
    answer = str(min(ss)) + " " + str(max(ss))
    return answer