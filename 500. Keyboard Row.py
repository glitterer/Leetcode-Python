class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row = "qwertyuiopQWERTYUIOP"
        second_row = "asdfghjklASDFGHJKL"
        third_row = "zxcvbnmZXCVBNM"
        final_ans = []
        for word in words:
            ans = []
            word_len = len(word)
            for alphabet in word:
                if alphabet in first_row:
                    ans.append(1)
                elif alphabet in second_row:
                    ans.append(2)
                else:
                    ans.append(3)
            print(ans)
            if ans.count(1) == word_len or ans.count(2) == word_len or ans.count(3) == word_len:
                final_ans.append(word)
        return final_ans