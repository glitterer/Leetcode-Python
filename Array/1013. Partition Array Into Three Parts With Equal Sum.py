class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        arr_sum = sum(arr)
        if arr_sum % 3 != 0:
            return False
        else:
            avg = arr_sum // 3
            ans = 0
            ans_list = []
            for i in arr:
                ans += i
                if ans == avg:
                    ans_list.append(1)
                    ans = 0
            # [0,0,0,0]을 처리하기 위해서 append(1)을 통한 sum이 3 이상인 것을 고려한다.
            return sum(ans_list) >= 3
