class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        count = 0
        for i in s[0:k]:
            if i in vowels:
                count += 1
        left, right, maxV = 0, k - 1, count
        while right < len(s) - 1:
            right += 1
            if s[right] in vowels:
                count += 1
            if s[left] in vowels:
                count -= 1
            left += 1
            maxV = max(maxV, count)
        return maxV
