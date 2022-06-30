class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        nums_dict = {}
        for i in nums:
            if i not in nums_dict.keys():
                nums_dict[i] = 1
            else:
                nums_dict[i] = nums_dict[i] + 1
        print(nums_dict)
        # lambda 함수 (x, -y) : +면, x에 대해서 먼저 오름차순 --> -면, y에 대해서 내림차순
        nums_dict_sort = sorted(nums_dict.items(), key = lambda x:(x[1], -x[0]))
        print(nums_dict_sort)
        
        ans = []
        for i, j in nums_dict_sort:
            for _ in range(j):
                ans.append(i)
        return ans
    
    
    '''
        # source: https://leetcode.com/problems/sort-array-by-increasing-frequency/discuss/2122372/one-linear-solution
        count = collections.Counter(nums)
        return sorted(nums, key = lambda x: (count[x], -x))
        '''
