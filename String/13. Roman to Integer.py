class Solution:
    def romanToInt(self, s: str) -> int:
        sym_val = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        sym_val_two = {"IV":"IIII", "IX": "IIIIIIIII", "XL":"XXXX", "XC":"XXXXXXXXX", "CD":"CCCC", "CM":"CCCCCCCCC"}
        
        ans = 0
        for roman_two in sym_val_two.keys():
            s = s.replace(roman_two, sym_val_two[roman_two])
        
        for i in s:
            ans += sym_val[i]
        
        return ans
