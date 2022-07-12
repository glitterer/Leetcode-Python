# Time complexity가 매우 안 좋음.. 나중에 수정 필요
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        ans = []
        if m*n < len(original):
            return ans
        elif m*n > len(original):
            return ans
        else:
            for i in range(m):
                temp = []
                for i in range(n):
                    temp.append(original[0])
                    original.pop(0)
                ans.append(temp)
            return ans
