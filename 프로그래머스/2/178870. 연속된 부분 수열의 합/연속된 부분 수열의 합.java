class Solution {
    public int[] solution(int[] sequence, int k) {
        int[] answer = {-1, sequence.length};
        int left = 0;
        int right = 0;
        int sum = sequence[right];
        
        while(left <= right && right < sequence.length){
            if(sum == k){
                if(right - left < answer[1] - answer[0]){
                    answer[0] = left;
                    answer[1] = right;
                }
                sum -= sequence[left++];
            }    
            else if (sum > k) {
                sum -= sequence[left++];
            }
            else if (right < sequence.length - 1){
                sum += sequence[++right];
            }
            else{
                break;
            }
        }
        return answer;
    }
}