class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            str_x = [i for i in str(x)]
            for i in range(len(str_x)//2):
                if i == len(str_x)-(i+1):
                    pass
                elif str_x[i] != str_x[len(str_x)-(i+1)]:
                    return False
                else:
                    pass
            return True
