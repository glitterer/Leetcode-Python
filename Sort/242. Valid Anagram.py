class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s_list = list(s)
        # t_list = list(t)
        # s_sort = sorted(s)
        # t_sort = sorted(t)
        # if sorted(s) == sorted(t):
        #     return True
        # else:
        #   return False
        return sorted(s) == sorted(t)
