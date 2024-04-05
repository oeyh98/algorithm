class Solution {
    
    public static int cal(int n) {
        int cnt = 0;
        
        for(int i = 1; i*i < n+1; i++){
            if(i * i == n) cnt++;
            else if(n % i == 0 ) cnt += 2;
        }
        
        return cnt;
    }

    public int solution(int number, int limit, int power) {
        int answer = 0;
        
        for(int i = 1; i <= number; i++){
            int calNum = cal(i);
            
            if(calNum > limit){
                calNum = power;
            }
            answer += calNum;
        }
        return answer;
    }
}