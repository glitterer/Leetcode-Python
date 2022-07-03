class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row = set("qwertyuiop") 
        # first = {"qwertyuiop"}
        second_row = set("asdfghjkl")
        third_row = set("zxcvbnm")
        '''
        playing with string/sets
        print(f'list: {list("aaaggeb")}')
        print(f'set: {set("aaaggeb")}')
        print(f'set: {{{"aaaggeb"}}}')
        print(f'set: {first}')
        '''
        final_ans = []
        for word in words:
            ans = set()
            # ans = {}
            for alphabet in word.lower():
                if alphabet in first_row:
                    ans.add(1)
                elif alphabet in second_row:
                    ans.add(2)
                else:
                    ans.add(3)
            if len(ans) == 1:
                final_ans.append(word)
        return final_ans
    
        # set --> append가 아니라 add로 원소 추가 
        # https://wikidocs.net/16044
        # k = {100, 105}
        # k.add(2)
        # --> k 는 {100, 105, 2}
