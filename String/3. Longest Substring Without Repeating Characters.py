class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pattern_cnt = []
        if s == "":
            return 0
        for i in range(len(s)):
            cnt = 0
            pattern = []
            j = i
            while True:
                if s[j] not in pattern:
                    pattern.append(s[j])
                    j += 1
                    cnt += 1
                elif s[j] in pattern:
                    pattern_cnt.append(len(pattern))
                    break
                
                if j > len(s)-1:
                    pattern_cnt.append(cnt)
                    break
        return max(pattern_cnt)
            
