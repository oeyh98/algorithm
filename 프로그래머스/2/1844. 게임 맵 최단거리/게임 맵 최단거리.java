import java.util.*;

class Solution {
    public int dfs(int[][] maps){
        int n = maps.length;
        int m = maps[0].length;
        
        int[] dx = {0, 0, 1, -1};
        int[] dy = {1, -1, 0, 0};
        
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[] {0, 0});
        
        while(!queue.isEmpty()){
            int[] node = queue.poll();
            int x = node[0];
            int y = node[1];
            
            if(x == (n-1) && y == (m-1)){
                return maps[x][y];
            }
            
            for(int i = 0; i < 4; i++){
                int nx = x + dx[i];
                int ny = y + dy[i];
                
                if(0 <= nx && nx < n && 0 <= ny && ny < m && maps[nx][ny] == 1){
                    maps[nx][ny] = maps[x][y] + 1;
                    queue.offer(new int[]{nx, ny});                    
                }
            }
        }
        return -1;
    }
        
    public int solution(int[][] maps) {
        return dfs(maps);
    }
}