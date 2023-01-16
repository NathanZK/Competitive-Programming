class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        length = len(words)
        letters = [[0 for i in range(length)] for i in range(26)]
        for i in range(len(words)):
            for j in range(len(words[0])):
                let = ord(words[i][j]) - 97
                letters[let][i] += 1

        dup = []
        for i in range(26):
            min_ = min(letters[i])
            while min_ > 0:
                dup.append(chr(i + 97))
                min_ -= 1

        return dup
