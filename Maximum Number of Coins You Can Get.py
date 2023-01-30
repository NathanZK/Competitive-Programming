class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        left, right = 0, len(piles) - 1
        piles.sort()
        maxCoins = 0
        while left < right:
            maxCoins += piles[right-1]
            left += 1
            right -=2

        return maxCoins
        
