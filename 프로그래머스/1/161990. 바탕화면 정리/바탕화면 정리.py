def solution(wallpaper):
    lux, luy = 51, 51
    rdx, rdy = 0, 0
    
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                if i < lux:
                    lux = i
                if j < luy:
                    luy = j
                if rdx < i + 1:
                    rdx = i + 1
                if rdy < j + 1:
                    rdy = j + 1
        
    
    return [lux, luy, rdx, rdy]