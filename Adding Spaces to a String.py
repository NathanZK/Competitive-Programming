class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        newString = [char for char in s]
        res = []
        i, j = 0, 0
        while i < len(newString) and j < len(spaces):
            if i == spaces[j]:
                res.append(" ")
                j += 1
            else:
                res.append(newString[i])
                i += 1

        res.append(s[i:])
        return "".join(res)
