class Solution {
    public int solution(String[] babbling) {
        int answer = 0;
        String[] as = {"aya", "ye", "woo", "ma"};
        String[] bs = {"ayaaya", "yeye", "woowoo", "mama"};
        
        for(String babble : babbling){
            for(String s:bs){
                babble = babble.replaceAll(s, "0");   
            }
            
            for(String s:as){
                babble = babble.replaceAll(s, "1");
            }
            
            if(babble.replaceAll("1", "").length() == 0){
                answer++;
            }
        }
        
        return answer;
    }
}