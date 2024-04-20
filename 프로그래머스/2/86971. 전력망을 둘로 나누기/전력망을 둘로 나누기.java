import java.util.*;

class Solution {
    static List<Integer>[] graph;
    static int minValue;
    
    public int solution(int n, int[][] wires) {
        graph = new ArrayList[n+1];
        minValue = Integer.MAX_VALUE;
        
        for(int i = 1; i < n+1; i++){
           graph[i] = new ArrayList<>(); 
        }
        
        for(int[] wire: wires){
            graph[wire[0]].add(wire[1]);
            graph[wire[1]].add(wire[0]);
        }
        
        for(int[] wire: wires){
            boolean[] visited = new boolean[n+1];
            
            graph[wire[0]].remove(Integer.valueOf(wire[1]));
            graph[wire[1]].remove(Integer.valueOf(wire[0]));
            
            int cnt = dfs(1, visited);
            int diff = Math.abs(cnt - (n - cnt));
            
            minValue = Math.min(minValue, diff);
            
            graph[wire[0]].add(wire[1]);
            graph[wire[1]].add(wire[0]);
        }
        
        
        return minValue;
    }
    
    static int dfs(int v, boolean[] visited){
        visited[v] = true;
        int cnt = 1;
        
        for(int node : graph[v]){
            if(visited[node] == false){
                cnt += dfs(node, visited);
            }
        }
        return cnt;
    }
}