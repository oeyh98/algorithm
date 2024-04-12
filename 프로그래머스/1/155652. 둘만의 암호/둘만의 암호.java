import java.util.*;

class Solution {
    public String solution(String s, String skip, int index) {
        String answer = "";
        Character[] alpha = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};
        List<Character> list = new ArrayList<>();
        
        for(int i = 0; i < alpha.length; i++) 
            list.add(Character.valueOf(alpha[i])); 
        
        for(int i = 0; i < skip.length(); i++) 
            list.remove(Character.valueOf(skip.charAt(i)));
        
        int size = list.size();
        for(int i = 0 ; i < s.length(); i++){
            int idx = list.indexOf(s.charAt(i)) + index;
            idx %= size;
            answer += Character.valueOf(list.get(idx));
        }
        return answer;
    }
}