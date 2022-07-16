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
        
        '''
        # 더 간단하고 정제된 코드
        ans = []
        cnt = 0
        if m*n != len(original):
            return ans
        else:
#             for i in range(m):
#                 temp = original[i*n:(i+1)*n]
#                 ans.append(temp)
#             return ans
            return [original[i*n:(i+1)*n] for i in range(m)]
            '''
