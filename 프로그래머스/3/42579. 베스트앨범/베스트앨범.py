def solution(genres, plays):
    answer = []    
    genres_count = {}
    plays_count = {}
    
    for i, genre in enumerate(genres):
        genres_count[genres[i]] = genres_count.get(genres[i], 0) + plays[i]
        plays_count[genres[i]] = plays_count.get(genres[i], []) + [(plays[i], i)]
        
    sorted_genres = sorted(genres_count.items(), key=lambda x: x[1], reverse=True)
        
    
    
    for (genre, total_play) in sorted_genres:
        plays_count[genre] = sorted(plays_count[genre], key=lambda x: (-x[0], x[1]))
        answer += [idx for (play, idx) in plays_count[genre][:2]]
    
    return answer
