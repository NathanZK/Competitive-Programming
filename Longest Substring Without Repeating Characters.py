class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        size = len(s)
        left, right = 0, 0
        letters = {}
        length, maxL = 0, 0
        
        for right in range(size):
            if s[right] not in letters:
                letters[s[right]] = right
            else:
                left = max(left, letters.get(s[right]) + 1)
                letters[s[right]] = right
                
            length = right - left + 1
            maxL = max(length, maxL)
            
        return maxL
                
                
        
