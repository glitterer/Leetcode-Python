class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        max_eat_num = int(len(candyType) / 2)
        candy_types = len(set(candyType))
        if candy_types < max_eat_num:
            return candy_types
        else:
            return max_eat_num
