import math
class Solution:
    def trimMean(self, arr: List[int]) -> float:
        '''
        arr.sort()
        ans = []
        print(len(arr))
        smallLeftOver = round(len(arr)*0.05)
        print(smallLeftOver)
        largeLeftOver = round(len(arr)*0.95) 
        print(largeLeftOver)
        for i in range(smallLeftOver, largeLeftOver):
            ans.append(arr[i])
        print(ans)
        print(len(ans))
        return sum(ans) / len(ans)
        '''
        arr.sort()
        exclude = round(len(arr)*0.05)
        new_arr = arr[exclude:-exclude]  # new_arr = arr[something:len(new_arr)-something]
        return sum(new_arr) / len(new_arr)
