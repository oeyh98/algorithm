class Solution {
    static void move(String[] park, int[] start, String direction, int len){
        if(direction.equals("N")){
            for(int i = 1; i <= len; i++){
                if(start[0] - i < 0 || park[start[0] - i].charAt(start[1]) == 'X') {
                    return;
                }
            }
            
            start[0] = start[0] - len;
        }
        else if(direction.equals("E")){
            for(int i = 1; i <= len; i++){
                if(start[1] + i >= park[0].length() || park[start[0]].charAt(start[1] + i) == 'X') {
                    return;
                }
            }
            
            start[1] = start[1] + len;
        }
        else if(direction.equals("S")){
            for(int i = 1; i <= len; i++){
                if(start[0] + i >= park.length || park[start[0] + i].charAt(start[1]) == 'X') {
                    return;
                }
            }
            
            start[0] = start[0] + len;
        }
        else if(direction.equals("W")){
            for(int i = 1; i <= len; i++){
                if(start[1] - i < 0 || park[start[0]].charAt(start[1] - i) == 'X') {
                    return;
                }
            }
            
            start[1] = start[1] - len;
        }
    }
    
    static void findStart(String[] park, int[] start){
        for(int i = 0; i < park.length; i++){
            for(int j = 0; j < park[0].length(); j++){
                if(park[i].charAt(j) == 'S'){
                    start[0] = i;
                    start[1] = j;
                    return;
                }
            }
        }
    }
    
    public int[] solution(String[] park, String[] routes) {
        int[] answer = new int[2];
        int[] start = new int[2];
        findStart(park, start);
        
        for(String route : routes){
            String[] r = route.split(" ");
            String direction = r[0];
            int len = Integer.parseInt(r[1]);
            move(park, start, direction, len);
        }
        
        answer[0] = start[0];
        answer[1] = start[1];
        
        return answer;
    }
}