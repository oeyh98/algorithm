import java.util.*;

class Solution {
    public String solution(String[] survey, int[] choices) {
        String answer = "";
        char[][] types = {{'R', 'T'}, {'C', 'F'}, {'J', 'M'}, {'A', 'N'}};
        int[] scores = {0, 3, 2, 1, 0, 1, 2, 3};
        Map<Character, Integer> hm = new HashMap<>();
        
        for(char[] type : types){
            hm.put(type[0], 0);
            hm.put(type[1], 0);
        }
        
        for(int i = 0; i < survey.length; i++){
            char s = (choices[i] < 4) ? survey[i].charAt(0) : survey[i].charAt(1);
            hm.put(s, hm.get(s) + scores[choices[i]]);
        }
        
        for(char[] type : types)
            answer += (hm.get(type[0]) >= hm.get(type[1])) ? type[0] : type[1];
    
        return answer;
    }
}