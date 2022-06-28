class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''
        nums1_set = list(set(nums1))
        nums2_set = list(set(nums2))
        ans = []
        if len(nums1_set) > len(nums2_set):
            for i in range(len(nums2_set)):
                if nums2_set[i] in nums1_set:
                    ans.append(nums2_set[i])
        else:
            for i in range(len(nums1_set)):
                if nums1_set[i] in nums2_set:
                    ans.append(nums1_set[i])
        return ans
        '''
    
    
        nums1_set = list(set(nums1))
        nums2_set = list(set(nums2))
        ans = []
        for i in range(len(nums2_set)):
            if nums2_set[i] in nums1_set:
                ans.append(nums2_set[i])
        return ans
