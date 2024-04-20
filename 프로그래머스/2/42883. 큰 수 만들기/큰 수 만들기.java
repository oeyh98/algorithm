import java.util.*;
class Solution {
    public String solution(String number, int k) {
        String answer = "";
        Stack<Character> stack = new Stack<>();
        int answerLen = number.length() - k;
        for(char num : number.toCharArray()){
            while(!stack.isEmpty() && k > 0 && stack.peek() < num){
                stack.pop();
                k--;
            }
            stack.push(num);
        }
        
        
        for(int i = 0; i < answerLen; i++){
            answer += stack.get(i);
        }
        return answer;
    }
}