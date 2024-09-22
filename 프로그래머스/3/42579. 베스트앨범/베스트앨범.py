def solution(genres, plays):
    answer = []
    genres_dic = {genre:0 for genre in genres}
    plays_dic = {genre:[] for genre in genres}
    
    for i in range(len(genres)):
        genres_dic[genres[i]] += plays[i]
        plays_dic[genres[i]] += [(i, plays[i])]
        
    sorted_dic = sorted(genres_dic.items(), key = lambda x:x[1], reverse = True)

    for genre, _ in sorted_dic:
        sorted_play = sorted(plays_dic[genre], key = lambda x: (-x[1], x[0])) 
        answer += [idx for idx, _ in sorted_play[:2]]
        
    return answer