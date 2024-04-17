import java.util.*;
class Solution {
    public int[] solution(String[] id_list, String[] report, int k) {
        int[] answer = new int[id_list.length];
        Map<String, HashSet<String>> map = new HashMap<>();
        Map<String, Integer> idxMap = new HashMap<>();
        for(int i = 0; i < id_list.length; i++){
            map.put(id_list[i], new HashSet<>());
            idxMap.put(id_list[i], i);
        }
        
        for(String r : report){
            String[] str = r.split(" ");
            String from = str[0];
            String to = str[1];
            
            map.get(to).add(from);
        }
        
        for(int i = 0; i < id_list.length; i++){
            HashSet<String> hs = map.get(id_list[i]);
            if(hs.size() >= k){
                for(String from : hs){
                    answer[idxMap.get(from)]++;
                }
            }
        }
        
        return answer;
    }
}