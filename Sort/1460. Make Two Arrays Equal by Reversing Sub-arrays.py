class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        # return set(target) == set(arr)
        
#         for i in target:
#             if target.count(i) != arr.count(i):
#                 return False
#         return True
    
        # target.sort()
        # arr.sort()
        # target == arr
#         target_sorted = sorted(target)
#         arr_sorted = sorted(arr)
#         return target_sorted == arr_sorted
        return sorted(target) == sorted(arr)
