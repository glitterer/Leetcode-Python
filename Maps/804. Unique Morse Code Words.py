class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        
        morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]        
        
        morse_res = []
        final_res = []
        for word in words:
            for alphabet in word:
                morse_res.append(morse_code[ord(alphabet)-97])
            final_res.append("".join(morse_res))
            morse_res = []
        return len(set(final_res))
