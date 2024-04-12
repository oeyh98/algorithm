import java.util.*;
class Solution {
    public int solution(int k, int[] tangerine) {
        int answer = 0;
        Map<Integer, Integer> hm = new HashMap<>();
        
        for(int t : tangerine){
            hm.put(t, hm.getOrDefault(t, 0) + 1);
        }
        
        List<Integer> keySet  = new ArrayList<>(hm.keySet());
        
        keySet.sort((o1, o2) -> hm.get(o2).compareTo(hm.get(o1)));
        
        
        for(int i = 0; i < keySet.size(); i++){
            k -= hm.get(keySet.get(i));
            answer += 1;
            
            if(k <= 0){
                break;
            }
        }
        return answer;
    }
}