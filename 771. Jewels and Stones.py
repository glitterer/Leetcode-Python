class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_set = set(jewels)
        cnt = 0
        for i in stones:
            if i in jewels_set:
                cnt += 1
            else:
                pass
        return cnt
