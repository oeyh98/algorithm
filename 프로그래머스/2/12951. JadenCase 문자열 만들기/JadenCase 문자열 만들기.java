class Solution {
    public String solution(String s) {
        String answer = "";
        String[] str = s.toLowerCase().split("");
    
        for(int i = 0; i < str.length; i++){
            if(answer.isEmpty() || answer.endsWith(" ")){
                str[i] = str[i].toUpperCase();
            }
            answer += str[i];
        }
        return answer;
    }
}