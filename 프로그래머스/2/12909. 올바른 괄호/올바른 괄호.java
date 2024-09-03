import java.util.*;
class Solution {
    boolean solution(String s) {
        boolean answer = true;
        Stack<Character> stack = new Stack<>();
        
        for(int i = 0; i < s.length(); i++){
            char str = s.charAt(i);
            if(str == '(')
                stack.push(str);
            else{
                if (stack.empty() || stack.peek() == ')'){
                    answer = false;
                    break;
                }
                else if (stack.peek() == '('){
                    stack.pop();
                }
            }
        }
        
        if(!stack.empty()){
            answer = false;
        }

        return answer;
    }
}