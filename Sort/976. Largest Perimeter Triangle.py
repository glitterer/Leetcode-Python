class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        print(nums)
        '''
        첫시도 --> 실패 --> 숫자 4개 이상도 주는지 모름...
        if nums[0] + nums[1] <= nums[2]:
            return 0
        else:
            return nums[0] + nums[1] + nums[2]
        '''
        '''
        ans = []
        for i in range(len(nums)-2):
            if nums[i] + nums[i+1] > nums[i+2]:
                ans.append(nums[i] + nums[i+1] + nums[i+2])
            else:
                ans.append(0)
        return max(ans)
        '''
        for i in range(len(nums)-2):
            if nums[i+2] + nums[i+1] > nums[i]:
                return nums[i] + nums[i+1] + nums[i+2]
        return 0
