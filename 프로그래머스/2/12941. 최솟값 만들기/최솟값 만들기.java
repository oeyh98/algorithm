import java.util.*;

class Solution
{
    public int solution(int []A, int []B)
    {
        int answer = 0;
        int leng = A.length;
        Arrays.sort(A);
        Arrays.sort(B);
        
        for(int i = 0; i < leng; i++){
            answer += (A[i] * B[leng - i - 1]);
        }

        return answer;
    }
}