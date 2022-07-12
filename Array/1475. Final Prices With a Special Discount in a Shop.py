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
