class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        
        def f(s) -> int:
            return s.count(min(s))
        
        fword = [f(word) for word in words]
        fqueries = [f(query) for query in queries]
        
        ans = []
        for q in fqueries:
            cnt = 0
            for w in fword:
                if q < w:
                    cnt += 1
            ans.append(cnt)
        
        return ans
