import java.util.*;

class Solution {
    public void dfs(List<String> result,  Map<String, PriorityQueue<String>> map, String src){
        while(map.containsKey(src) && !map.get(src).isEmpty()){
            dfs(result, map, map.get(src).poll());
        }
        result.add(0, src);
    }
    
    public String[] solution(String[][] tickets) {
        List<String> result = new ArrayList<>();
        Map<String, PriorityQueue<String>> map = new HashMap<>();
        
        for(String[] ticket : tickets){
            String src = ticket[0];
            String des = ticket[1];
            map.putIfAbsent(src, new PriorityQueue<String>());
            map.get(src).add(des);
        }
        
        dfs(result, map, "ICN");
        
        String[] answer = new String[result.size()];
        for(int i = 0; i < result.size(); i++){
            answer[i] = result.get(i);
        }
        
        return answer;
    }
}