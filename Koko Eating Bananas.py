class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 0, max(piles) + 1

        while left + 1 < right:
            mid = (left) + (right - left)//2
            if self.finish(piles, mid) > h:
                left = mid
            else:
                right = mid

        return right

    def finish(self, piles, mid):
        totalHour = 0
        for p in piles:
            totalHour += math.ceil(p/mid)

        return totalHour
