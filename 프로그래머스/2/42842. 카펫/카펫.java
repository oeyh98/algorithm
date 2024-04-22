class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = new int[2];
        int carpet = brown + yellow;
        
        for(int i = 3; i < carpet; i++){
            int col = carpet/i;
            int row = i;
            
            if(col < row) continue;
            
            if((col-2) * (row-2) == yellow){
                answer[0] = col;
                answer[1] = row;
                break;
            }
        }
        return answer;
    }
}