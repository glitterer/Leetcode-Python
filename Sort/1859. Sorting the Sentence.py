class Solution:
    def sortSentence(self, s: str) -> str:
        
        s_list = list(map(str, s.split()))
        # print(s.split())
        
        ans = []
        # print(s_list[1][:-2:-1])
        
        for i in range(len(s_list)):
            ans.append(s_list[i][:-2:-1] + s_list[i][0:-1])
        ans.sort()
        # print(ans)
        
        finAns = ' '.join(ans)
        
        for strings in finAns:
            if strings.isnumeric() == True:
                continue
            else:
                ans.append(strings)
            
        return ''.join(ans[len(s_list):])
