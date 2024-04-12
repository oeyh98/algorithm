class Solution {
    public int[] solution(String[] wallpaper) {
        int lux = Integer.MAX_VALUE, luy = Integer.MAX_VALUE;
        int rdx = 0, rdy = 0;
        
        for(int i = 0; i < wallpaper.length; i++){
            for(int j = 0; j < wallpaper[i].length(); j++){
                char temp = wallpaper[i].charAt(j);
                if(temp == '#'){
                    lux = Math.min(lux, i);
                    luy = Math.min(luy, j);
                    rdx = Math.max(rdx, i);
                    rdy = Math.max(rdy, j);
                }
            }
        }
        
        
        int[] answer = {lux, luy, rdx + 1, rdy + 1};
        return answer;
    }
}