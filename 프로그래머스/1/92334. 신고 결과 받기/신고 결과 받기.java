import java.util.*;
class Solution {
    public int[] solution(String[] id_list, String[] reports, int k) {
        int[] answer = new int[id_list.length];
        Map<String, HashSet<String>> reportMap = new HashMap<>();
        Map<String, Integer> idxMap = new HashMap<>();
        
        for(int i = 0; i < id_list.length; i++){
            reportMap.put(id_list[i], new HashSet<>());
            idxMap.put(id_list[i], i);
        }
        
        for(String report : reports){
            String[] temp = report.split(" ");
            reportMap.get(temp[1]).add(temp[0]);
        }
        
        for(int i = 0; i < id_list.length; i++){
            HashSet<String> hs = reportMap.get(id_list[i]);
            if(k <= hs.size()){
                for(String value : hs){
                    answer[idxMap.get(value)]++;    
                }
                
            }
        }
        
        
                
        return answer;
    }
}