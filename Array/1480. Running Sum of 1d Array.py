class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        '''
        def runningSum(self,nums,i=1):
            if(i==len(nums)):
                return nums[:]
            nums[i]+=nums[i-1]
            return self.runningSum(nums,i+1)
        '''
        
        # final_ans = []
        # for i in range(len(nums)):
        #     ans_1 = []
        #     for j in range(i+1):
        #         ans_1.append(nums[j])
        #     final_ans.append(sum(ans_1))
        # return final_ans
    
        for i in range(len(nums)):
            if i == 0:
                nums[i] = nums[0]
            else:
                nums[i] = nums[i-1] + nums[i]
        return nums
