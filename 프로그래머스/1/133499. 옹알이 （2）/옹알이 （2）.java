class Solution {    
    public int solution(String[] babbling) {
        int answer = 0;
        String[] canBabble = {"aya", "ye", "woo", "ma"};
        String[] doubleBabble = {"ayaaya", "yeye", "woowoo", "mama"};
        
        for(int i = 0; i < babbling.length; i++){
            for(String db: doubleBabble){
                babbling[i] = babbling[i].replace(db, "*");
            }
            
            for(String cb: canBabble){
                babbling[i] = babbling[i].replace(cb, " ");
            }
            babbling[i] = babbling[i].replace(" ", "");
            
            if(babbling[i].length() == 0) answer++;
        }
            
        return answer;
    }
}