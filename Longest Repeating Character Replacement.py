class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charMap = {}
        left = 0
        longest, maxElem = 0, 0

        for right in range(len(s)):
            charMap[s[right]] = charMap.get(s[right], 0) + 1
            maxElem = max(maxElem, charMap[s[right]])
            
            while right - left + 1 - maxElem > k:
                charMap[s[left]] -= 1
                if charMap[s[left]] == 0:
                    del charMap[s[left]]
                left += 1

            longest = max(longest, right - left + 1)

        return longest
