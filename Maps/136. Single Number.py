class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        maps = {}
        for i in nums:
            if i not in maps.keys():
                maps[i] = 1
            else:
                maps[i] += 1
    
        for k, v in maps.items():
            if v == 1:
                # print(maps)
                return k
