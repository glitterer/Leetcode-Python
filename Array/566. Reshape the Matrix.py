class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        decompose_2d = []
        final_ans = []
        for i in mat:
            for j in i:
                decompose_2d.append(j)

        decompose_2dlen = len(decompose_2d)

        if decompose_2dlen%r != 0:
            return mat
        else:
            for i in range(r):
                temp = decompose_2d[i*decompose_2dlen//r:i*decompose_2dlen//r+decompose_2dlen//r]
                final_ans.append(temp)
            return final_ans
        
        
        '''
        class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        # 현재 오류 코드
        # [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
        # 3
        # 5
        decompose_2d = []
        final_ans = []
        for i in mat:
            for j in i:
                decompose_2d.append(j)
        # print(decompose_2d)\
        decompose_2dlen = len(decompose_2d)
        if len(decompose_2d)%r != 0:
            return mat
        else:
            while True:
                temp = []
                for i in range(decompose_2dlen//r):
                    temp.append(decompose_2d[i])
                final_ans.append(temp)
                
                for i in range(decompose_2dlen//r):
                    decompose_2d.pop(0)
                    
                if len(decompose_2d) == 0:
                    break
            return final_ans
        '''
