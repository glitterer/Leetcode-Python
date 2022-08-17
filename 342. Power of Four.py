class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        #-2147483648 runtime error
        binaryNum = bin(n)
        bin_num = []
        cnt = 0
        if n > 0:
            for i in binaryNum:
                if cnt > 1:
                    bin_num.append(int(i))
                cnt += 1
        else:
            return False
                
        # n = 1
        if len(bin_num) == 1:
            return True
        
        # n != 1
        if len(bin_num) % 2 == 0:
            return False
        else:
            if bin_num.count(1) != 1:
                return False
        return True
