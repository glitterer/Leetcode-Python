class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # reverse the nums list
        cnt = 0
        for i in nums[::-1]:
            if cnt == 0:
                nums.clear()
                nums.append(i)
            else:
                nums.append(i)
            cnt += 1
        
        # add k amount of numbers
        for i in range(k): 
            nums.append(nums[i])
        
        # reverse again (to its original form)
        cnt = 0
        for i in nums[::-1]:
            if cnt == 0:
                nums.clear()
                nums.append(i)
            else:
                nums.append(i)
            cnt += 1
        
        # pop the k amount of numbers
        for i in range(k):
            nums.pop()    
