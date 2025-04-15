import java.util.*;

class Solution {
    void bfs(int cur, int n, int[][] computers, boolean visited[]){
        Queue<Integer> queue = new LinkedList<>();
        queue.add(cur);
        
        while(!queue.isEmpty()){        
            int node = queue.poll();
            visited[node] = true;

            for(int i = 0; i < n; i++){
                if(computers[node][i] == 1 && i != node && !visited[i]){
                    queue.add(i);
                }
            }
        }
    }
    public int solution(int n, int[][] computers) {
        int answer = 0;
        boolean[] visited = new boolean[n];
        
        for(int i = 0; i < n; i++){
            visited[i] = false;
        }
        
        for(int i = 0; i < n; i++){
            if(!visited[i]){
                answer++;
                bfs(i, n, computers, visited);
            }
        }
        
        return answer;
    }
}