import java.util.*;

class Solution {
    public String solution(String s) {
        String answer = "";

        
        String[] splited = s.split(" ");
        int[] num = new int[splited.length];
        for(int i = 0; i < splited.length; i++){
            num[i] = Integer.parseInt(splited[i]);
        }
        
        int maxValue = num[0];
        int minValue = num[0];
        
        for(int i = 1; i < splited.length; i++){
            maxValue = Math.max(maxValue, num[i]);
            minValue = Math.min(minValue, num[i]);
        }
        
        answer += Integer.toString(minValue);
        answer += " ";
        answer += Integer.toString(maxValue);
        
        return answer;
    }
}