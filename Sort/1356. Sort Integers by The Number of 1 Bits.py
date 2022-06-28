class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        
        '''
        # [10000, 10000]에서 오류가 생기는 코드
        # dictionary를 list로 바꿔야 한다...
        dic = {}
        arr.sort()
        for i in arr:
            dic[i] = bin(i)[2:]
            dic[i] = dic[i].count('1')
        print(dic)
        sort_dic = sorted(dic.items(), key=lambda x:x[1])
        # print(sort_dic)
        return [i[0] for i in sort_dic]
        '''
        ans = [(bin(i).count('1'), i) for i in arr]
        # ans = []
        # for i in arr:
        #     ans.append((bin(i).count('1'), i))
        print(ans)
        ans.sort()
        return [j[1] for j in ans]
