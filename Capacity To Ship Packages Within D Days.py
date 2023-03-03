class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights) - 1, sum(weights) + 1

        while left + 1 < right:
            mid = (left + right)//2
            if self.daysTaken(weights, mid) > days:
                left = mid
            else:
                right = mid

        return right

    def daysTaken(self, weights, capacity):
        days = 0
        loaded = 0

        for w in weights:
            loaded += w
            if loaded > capacity:
                days += 1
                loaded = w

        days += 1
        return days



        
