class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        final_ans = []
        for i in range(len(nums)):
            ans_1 = []
            for j in range(i+1):
                ans_1.append(nums[j])
            final_ans.append(sum(ans_1))
        return final_ans
