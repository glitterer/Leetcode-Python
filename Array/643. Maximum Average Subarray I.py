class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # first_sum = sum(nums[0:k])
        # sums_list = []
        # sums_list.append(first_sum)
        # for i in range(len(nums)-k):
        #     print(i)
        #     second_sum = sums_list[i] - nums[i] + nums[i+k]
        #     sums_list.append(second_sum)
        # return max(sums_list)/k
    
     
        now = sum(nums[0:k])
        best = now
        for i in range(len(nums)-k):
            now = now - nums[i] + nums[i+k]
            best = max(now, best)
        return best/k
    
    
        # best = 0
        # now = sum(nums[0:k])
        # best = now
        # for i in range(k,len(nums)):
        #     now += nums[i] - nums[i-k]
        #     best = max(best,now)
        # return best/k
