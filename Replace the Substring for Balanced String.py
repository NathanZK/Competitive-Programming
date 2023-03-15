class Solution:
    def balancedString(self, s: str) -> int:
        count = Counter(s)
        left, size = 0, len(s)//4
        minSub = len(s)

        for right in range(len(s)):  
            count[s[right]] = count.get(s[right], 0) - 1

            while count['W'] <= size and count['Q'] <= size and count['E'] <= size and count['R'] <= size and left < len(s):
                minSub = min(minSub, right - left + 1)
                count[s[left]] = count.get(s[left], 0) + 1
                left += 1
            
        return minSub

        
