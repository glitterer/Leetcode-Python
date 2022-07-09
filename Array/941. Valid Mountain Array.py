class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        # if len(arr) < 3:
        #     return False
        # if len(arr[0:arr.index(max(arr))]) == 0 or (len(arr)-1 - arr.index(max(arr))) == 0:
        #     return False
        # for up in range(arr.index(max(arr))):
        #     if arr[up] >= arr[up+1]:
        #         return False
        # for down in range(len(arr)-1 - arr.index(max(arr))):
        #     if arr[arr.index(max(arr))+down] <= arr[arr.index(max(arr))+down+1]:
        #         return False
        # return True
    
    
        # up
        i = 0
        while True:
            if i == len(arr)-1:
                return False
            else:
                if arr[i] >= arr[i+1]:
                    break
                else:
                    i += 1
    
        if i == 0: #올라가는게 없을 때
            return False
        
        # down
        while True:
            if i == len(arr)-1:
                break
            else:
                if arr[i] <= arr[i+1]:
                    return False
                else:
                    i += 1
        
        return True
