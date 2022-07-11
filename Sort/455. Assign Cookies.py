class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort() 
        i, j = 0, 0
        # i = 0 # 현재 아이
        # j = 0 # 현재 쿠키
        
        while(len(g)>i and len(s)>j):
            if s[j] >= g[i]:
                i += 1
            j += 1
        return i
