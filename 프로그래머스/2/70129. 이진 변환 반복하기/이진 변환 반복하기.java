class Solution {
    public int[] solution(String s) {
        int zeroCnt = 0;
        int transCnt = 0;
        
        while(1 < s.length()){
            transCnt++; 
            
            for(int i=0; i < s.length(); i++){
                if(s.charAt(i) == '0'){
                    zeroCnt++;
                }
            }

            s = s.replace("0", "");
            
            s = Integer.toBinaryString(s.length());
        }
        
        
        int[] answer = {transCnt, zeroCnt};
        return answer;
    }
}