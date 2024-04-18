import java.util.*; 
class Solution {
    static List<String> list = new ArrayList<>();
    static final String[] chr = {"A", "E", "I", "O", "U"};
    
    public int solution(String word) {
        int answer = 0;
        
        dfs("", 0);
        
        for(int i = 0; i < list.size(); i++){
            if(list.get(i).equals(word)){
                answer = i;
                break;
            }
        }
        return answer;
    }
    public static void dfs(String str, int depth){
        list.add(str);
        if(depth == 5) return;
        
        for(int i = 0; i < 5; i++){
            dfs(str+chr[i], depth + 1);
        }
    };
}