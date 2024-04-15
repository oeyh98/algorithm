class Solution {
    public int solution(String s) {
        int answer = 0;
        int prev = 0;
        String[] splited = s.split(" ");
        
        for(String str:splited){
            if(!str.equals("Z")){
                int num = Integer.parseInt(str);
                answer += num;
                prev = num;
            }
            
            else answer -= prev;
        }
        
        
        return answer;
    }
}