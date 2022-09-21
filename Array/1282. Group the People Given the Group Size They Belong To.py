class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        sorted_groupsize = sorted(groupSizes)
        set_groupsize = list(set(groupSizes))
        res = []
        for i in range(len(set_groupsize)):
            res.append([])
            
        for k, v in enumerate(groupSizes):
            for i in range(len(set_groupsize)):
                if v == set_groupsize[i]:
                    res[i].append(k)
        
        ans = []
        for i in range(len(res)):
            if len(res[i]) > set_groupsize[i]:
                temp_list = []
                for k in range(len(res[i])//set_groupsize[i]):
                    temp_list.append(res[i][k*set_groupsize[i]:k*set_groupsize[i]+set_groupsize[i]])
                ans.extend(temp_list)
            else:
                ans.append(res[i])
        print(ans)
        return ans
