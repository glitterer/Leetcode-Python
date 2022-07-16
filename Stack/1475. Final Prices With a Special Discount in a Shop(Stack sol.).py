class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:                
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
