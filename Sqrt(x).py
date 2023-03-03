class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x // 2 + 1
        
        while left <= right:
            mid = (left + right) // 2
            if mid**2 <= x < (mid+1)**2:
                return mid
            elif mid**2 < x:
                left = mid + 1
            else:
                right = mid - 1
