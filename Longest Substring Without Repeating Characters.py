class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return n
        l, r = 0, 0
        letters = {}
        length, maxL = 0, 0
        while r < n:
            if s[r] not in letters:
                letters[s[r]] = r
                r += 1
            else:
                if letters.get(s[r]) >= l:
                    l = letters.get(s[r]) + 1
                letters[s[r]] = r
                r += 1
            length = r - l
            maxL = max(length, maxL)
        return maxL
