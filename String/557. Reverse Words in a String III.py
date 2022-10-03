class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        print(words)
        ans = []
        for i in words:
            ans.append(i[::-1])
        return ' '.join(ans)
