class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_code = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..",
                      "e": ".", "f": "..-.", "g": "--.", "h": "....",
                      "i": "..", "j": ".---", "k": "-.-", "l": ".-..",
                      "m": "--", "n": "-.", "o": "---", "p": ".--.",
                      "q": "--.-", "r": ".-.", "s": "...", "t": "-",
                      "u": "..-", "v": "...-", "w": ".--", "x": "-..-",
                      "y": "-.--", "z": "--.."}
        morse_res = []
        final_res = []
        for word in words:
            for alphabet in word:
                morse_res.append(morse_code[alphabet])
            final_res.append("".join(morse_res))
            morse_res = []
        return len(set(final_res))
