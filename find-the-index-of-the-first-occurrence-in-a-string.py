class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1

        LPS = self.KMP(needle)
        p1, p2 = 0, 0

        while p1 < len(haystack):
            if haystack[p1] == needle[p2]:
                p1 += 1
                p2 += 1
            elif p2 == 0:
                p1 += 1
            else:
                p2 = LPS[p2-1]

            if p2 == len(needle):
                return p1 - p2

        return -1


    def KMP(self, word):
        n = len(word)
        LPS = [0 for _ in range(len(word))]

        left, right = 0, 1
        while right < n:
            if word[left] == word[right]:
                LPS[right] = left + 1
                left += 1
                right += 1

            else:
                if left == 0:
                    right += 1
                else:
                    left = LPS[left-1]

        return LPS