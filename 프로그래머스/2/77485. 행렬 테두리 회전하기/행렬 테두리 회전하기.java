class Solution {
    public int[] solution(int rows, int columns, int[][] queries) {
        int[] answer = new int[queries.length];
        int[][] matrix = new int[rows][columns];
        
        for(int i = 0; i < rows; i++){
            for(int j = 0; j < columns; j++){
                matrix[i][j] = (j + 1) + (i * columns);
            }
        }
        
        for(int i = 0; i < queries.length; i++){
            answer[i] = rotate(matrix, queries[i]);
        }
        
        return answer;
    }
    
    static int rotate(int[][] matrix, int[] query){
        int r1 = query[0]-1;
        int c1 = query[1]-1;
        int r2 = query[2]-1;
        int c2 = query[3]-1;
        int temp = matrix[r1][c2];
        int minValue = temp;
        
        for(int i = c2; i > c1; i--){ 
            matrix[r1][i] = matrix[r1][i-1];
            minValue = Math.min(minValue, matrix[r1][i]);
        }
        for(int i = r1; i < r2; i++){ 
            matrix[i][c1] = matrix[i+1][c1];
            minValue = Math.min(minValue, matrix[i][c1]);
        }
        for(int i = c1; i < c2; i++){ 
            matrix[r2][i] = matrix[r2][i+1];
            minValue = Math.min(minValue, matrix[r2][i]);
        }
        for(int i = r2; i > r1+1; i--){ 
            matrix[i][c2] = matrix[i-1][c2];
            minValue = Math.min(minValue, matrix[i][c2]);
        }
        matrix[r1+1][c2] = temp;
        
        
        return minValue;
    }
}