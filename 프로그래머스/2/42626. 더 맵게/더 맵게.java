import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        
        for(int s : scoville){
            pq.add(s);
        }
        if(pq.peek() >= K) return answer;
        
        while(pq.size() >= 2){
            pq.add(pq.poll() + pq.poll()*2);
            answer++;
            if(pq.peek() >= K) return answer;
        }
        return -1;
    }
}