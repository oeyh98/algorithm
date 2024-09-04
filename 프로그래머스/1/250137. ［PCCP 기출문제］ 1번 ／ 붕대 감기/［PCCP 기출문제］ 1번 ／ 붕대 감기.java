class Solution {
    public int solution(int[] bandage, int health, int[][] attacks) {
        int maxHealth = health;
        int idx = 0;
        int cnt = 0; 
        
        for(int t = 0; t <= attacks[attacks.length -1][0]; t++){
            if(t == attacks[idx][0]){
                cnt = 0;
                health -= attacks[idx][1];
                idx++;
                if(health <= 0) return -1;
            }
            
            else{
                cnt++;
                health += bandage[1];
                if(cnt == bandage[0]) {
                    health += bandage[2];
                    cnt = 0;
                };
                if(maxHealth < health) health = maxHealth;
            }
        }
        return health;
    }
}