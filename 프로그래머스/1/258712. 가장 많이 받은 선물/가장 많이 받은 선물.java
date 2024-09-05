import java.util.*;

class Solution {
    public int solution(String[] friends, String[] gifts) {
        int answer = 0;
        Map<String, Integer> idxMap = new HashMap<>();
        int[] score = new int[friends.length];
        int[][] record = new int[friends.length][friends.length];
        
        for (int i = 0; i < friends.length; i++) {
            idxMap.put(friends[i], i);
        }
        
        for (String g : gifts) {
            String[] gift = g.split(" ");
            
            score[idxMap.get(gift[0])]++;
            score[idxMap.get(gift[1])]--;
            record[idxMap.get(gift[0])][idxMap.get(gift[1])]++;
        }

       
       for (int i = 0; i < friends.length; i++) {
           int cnt = 0;
           for (int j = 0; j < friends.length; j++) {
                if(i == j) continue;
               if (record[i][j] > record[j][i]) cnt++;
               else if (record[i][j] == record[j][i] && score[i] > score[j]) cnt++; 
           }
           answer = Math.max(cnt, answer);
       }
        return answer;
    }
}
