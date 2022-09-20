class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        res = 0
        while len(piles) != 0:
            res += piles[-2]
            del piles[-2]
            del piles[-1]
            del piles[0]
        return res
