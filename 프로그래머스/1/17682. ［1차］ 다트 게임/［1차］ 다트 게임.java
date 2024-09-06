class Solution {
    public int solution(String dartResult) {
        int answer = 0;
        int[] score = new int[3];
        char[] dart = dartResult.toCharArray();
        int idx = -1;
        
        for(int i = 0; i < dart.length; i++){
            if(dart[i] == 'S'){
                continue;
            }
            else if(dart[i] == 'D'){
                score[idx] = (int)Math.pow(score[idx], 2);
            }
            else if(dart[i] == 'T'){
                score[idx] = (int)Math.pow(score[idx], 3);
            }
            
            else if(dart[i] == '*'){
                score[idx] *= 2;
                
                if(0 <= idx-1){
                    score[idx-1] *= 2;
                }
            }
            
            else if(dart[i] == '#'){
                score[idx] *= (-1);
            }
            
            else{
                idx++;
            
                if(dart[i] == '1' && i+1 < dart.length && dart[i+1] == '0'){
                    i++;
                    score[idx] = 10;
                }
                else{
                    score[idx] = Integer.parseInt(String.valueOf(dart[i]));
                }
            }
        }
        
        
        for(int s : score){
            answer += s;
        }
        
        return answer;
    }
}