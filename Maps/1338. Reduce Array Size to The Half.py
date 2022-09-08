class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        total_length = len(arr)
        total_length_copy = total_length
        arr_map = Counter(arr)
        arr_map_sorted = sorted(arr_map.items(), key=lambda x:x[1], reverse=True)
        res = 0
        for key, value in arr_map_sorted:
            total_length_copy -= value
            res += 1
            if total_length_copy <= total_length//2:
                break
        
        return res
