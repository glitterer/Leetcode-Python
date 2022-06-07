class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        output = 0
        n = len(tickets)
        for i in range(n):
            if tickets[i] < tickets[k]:
                output += tickets[i]
            else:
                if i<=k:
                    output += tickets[k]
                else:
                    output += tickets[k] - 1
        return output
        
        
'''    
# Java
class Solution {
    public int timeRequiredToBuy(int[] tickets, int k) {
      int output = 0;
      int n = tickets.length;
      for  (int i = 0;i<n;i++){
          if(tickets[i] < tickets[k]){
              output += tickets[i];
          }else{
                if(i <= k){
                  output += tickets[k];
              }else { 
                  output += tickets[k] - 1;
              } 
          }

      }
      return output;
    }
}
'''
'''
# Source: "discussion"
        n = len(tickets)
        item = tickets[k]
        time = 0
        
        while tickets[k] != 0:
            for i in range(n):
                if tickets[i] > 0:
                    tickets[i] -= 1
                    time += 1
                
                if i == k and tickets[i] == 0:
                    return time
        
        return time
        '''
