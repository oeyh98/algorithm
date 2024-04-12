import java.util.*;

class Solution {
    public String[] solution(String[] players, String[] callings) {
        Map<String, Integer> rankMap = new HashMap<>();
        
        for(int i = 0; i < players.length; i++) rankMap.put(players[i], i);
        for(String calling : callings){
            int idx = rankMap.get(calling);
            String temp = players[idx];
            players[idx] = players[idx -1];
            players[idx - 1] = temp;
            
            rankMap.put(players[idx -1], idx - 1);
            rankMap.put(players[idx], idx);
        }
        return players;
    }
}