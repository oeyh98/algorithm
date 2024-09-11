class Solution {
    public int solution(int n, int m, int[] section) {
        int cnt = 0;
        int[] wall = new int[n];
        
        for(int i = 0; i < n; i++){
            wall[i] = 1;
        }
        
        for(int s : section){
            wall[s-1] = 0;
        }
        
        for(int i = 0; i < n; i++){
            if(wall[i] == 0){
                cnt++;
                for(int j = 0; j < m; j++){
                    if(i+j >= n) break;                                       
                    wall[i+j] = 1;
                    
                }
            }
        }
        
        return cnt;
    }
}