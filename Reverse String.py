class Solution:
    def reverseString(self, s: List[str]) -> None:
        self.revString(s, 0, len(s) - 1)

    def revString(self, s, left, right):
        if left >= right:
            return s

        s[left], s[right] = s[right], s[left]    
        self.revString(s, left+1, right - 1)
        
