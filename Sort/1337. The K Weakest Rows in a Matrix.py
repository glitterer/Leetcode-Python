class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        '''
        soldier_count = {}
        for i in range(len(mat)):
            soldier_count[i] = mat[i].count(1)
        sortsoldier=sorted(soldier_count.items(), key=lambda x:x[1])
        return [i[0] for i in sortsoldier][:k]
        '''
        '''
        arr = []        
        for key, row  in enumerate(mat):
            row_count = row.count(1)
            arr.append((key, row_count))
        sortsoldier = sorted(arr, key=lambda x:x[1])
        return [i[0] for i in sortsoldier][:k]
        '''
        # count 대신에 sum
        arr = [(key, row.count(1)) for key, row in enumerate(mat)]
        sortsoldier = sorted(arr, key=lambda x:x[1])
        return [i[0] for i in sortsoldier][:k]
