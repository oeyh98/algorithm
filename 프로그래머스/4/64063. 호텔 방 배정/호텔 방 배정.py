import sys
sys.setrecursionlimit(10 ** 6)

def solution(k, room_number):
    room_dic = {}
    answer = []
    
    def get_room_num(x):
        if x not in room_dic:
            room_dic[x] = x + 1
            
            return x
        next_room = get_room_num(room_dic[x])
        room_dic[x] = next_room
        return next_room
    
    for num in room_number:
        answer.append(get_room_num(num - 1) + 1)
    return answer