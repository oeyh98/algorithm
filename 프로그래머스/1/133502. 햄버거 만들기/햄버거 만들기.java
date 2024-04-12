import java.util.*;
class Solution {
    public int solution(int[] ingredient) {
        int answer = 0;
        int idx = 0;
        int[] stack = new int[ingredient.length];
        
        for(int ingred : ingredient){
            stack[idx] = ingred;
            // System.out.println(Arrays.toString(stack));
            if(idx >= 3 
              && stack[idx] == 1
              && stack[idx -1] == 3
              && stack[idx -2] == 2
              && stack[idx -3] == 1){
                // System.out.println("pop!");
                answer++;
                idx -= 4;
            }
            
            idx++;
        }
        return answer;
    }
}