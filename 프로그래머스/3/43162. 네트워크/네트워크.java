import java.util.*;

class Solution {
    boolean[] visited;
    
    void dfs(int cur, int n, int[][] computers){
        Queue<Integer> queue = new LinkedList<>();   
        queue.add(cur);
        
        while(!queue.isEmpty()){
            int node = queue.poll();
            for(int i = 0; i < n; i++) {
                if(computers[node][i] == 1 && !visited[i]){
                    visited[i] = true;
                    queue.add(i);
                }
            }
        }
    }    
    public int solution(int n, int[][] computers) {
        int answer = 0;
        visited = new boolean[n];
        
        for(int i = 0; i < n; i++){
            if(!visited[i]){
                visited[i] = true;
                dfs(i, n, computers);
                answer++;
            }
        }
        return answer;
    }
}