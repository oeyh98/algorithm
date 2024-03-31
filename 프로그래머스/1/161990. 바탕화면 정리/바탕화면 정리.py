def solution(wallpaper):
    lux, luy = 51, 51
    rdx, rdy = 0, 0
    
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                if lux > i:
                    lux = i
                if luy > j:
                    luy = j
                if rdx < i:
                    rdx = i
                if rdy < j:
                    rdy = j
    
    return [lux, luy, rdx + 1, rdy + 1]