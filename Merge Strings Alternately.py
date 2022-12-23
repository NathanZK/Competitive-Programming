class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        point = 0

        while point < len(word1) and point < len(word2):
            res.append(word1[point])
            res.append(word2[point])

            point += 1

        if point == len(word1):
            res.append(word2[point:])
        elif point == len(word2):
            res.append(word1[point:])

        return "".join(res)
