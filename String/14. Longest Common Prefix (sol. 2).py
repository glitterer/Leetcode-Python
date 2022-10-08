class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = min([len(i) for i in strs])
        
        ans = []
        for i in range(min_len):
            check = 0
            for j in range(len(strs)-1):
                if strs[0][i] == strs[j+1][i]:
                    check = 0
                else:
                    check = 1
                    break
            if check == 0:
                ans.append(strs[0][i])
            else:
                break
        return ''.join(ans)
