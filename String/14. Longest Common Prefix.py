class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = 0
        for i in range(len(strs)):
            if len(strs[i]) == 0:
                return ""
            if min_len == 0:
                min_len = len(strs[i])
            else:
                if min_len > len(strs[i]):
                    min_len = len(strs[i])
                else:
                    pass
        
        ans = []
        for i in range(min_len):
            check = 0
            for j in range(len(strs)-1):
                if strs[0][i] == strs[j+1][i]:
                    check = 0
                else:
                    return ''.join(ans)
            if check == 0:
                ans.append(strs[0][i])
            else:
                pass
        return ''.join(ans)
