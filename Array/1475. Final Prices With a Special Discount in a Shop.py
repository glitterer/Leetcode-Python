class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans = []
        prices_len = len(prices)
        for i in range(prices_len-1):
            add_check = 0
            for j in range(i+1,prices_len):
                if prices[i] >= prices[j]:
                    ans.append(abs(prices[i]-prices[j]))
                    add_check += 1
                    break
            if add_check == 0:
                ans.append(prices[i])
        ans.append(prices[prices_len-1])
        return ans
        
        '''
        # answer from Discussion
        class Solution:
            def finalPrices(self, prices: List[int]) -> List[int]:
                mono = []

                for i, p in enumerate(prices):
                    while mono and prices[mono[-1]] >= p:
                        prices[mono.pop()] -= p
                    mono.append(i)
                return prices
        '''
                
        '''
        # Stack
        ans = []
        stack = []
        for i in range(len(prices)):
            cnt = 1
            while cnt != len(prices)-i:
                stack.append(prices[i+cnt])
                if stack[-1] <= prices[i]:
                    ans.append(abs(prices[i]-stack[-1]))
                    stack.pop()
                    break
                stack.pop()
                cnt += 1
            if len(ans) != i+1:
                ans.append(prices[i])
        return ans   
        '''
