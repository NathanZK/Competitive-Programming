class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        minRadius = 0
        heaters.sort()

        for n in houses:
            closeIdx = self.findClosestHeater(n, heaters)

            if closeIdx == len(heaters) - 1:
                minRadius = max(minRadius, n - heaters[closeIdx])
            else:
                minDist = min(abs(n-heaters[closeIdx]), abs(n - heaters[closeIdx+1]))
                minRadius = max(minRadius, minDist)

        return minRadius

    def findClosestHeater(self, n, heaters):
        left, right = -1, len(heaters)

        while left + 1 < right:
            mid = (left + right)//2

            if n < heaters[mid]:
                right = mid
            else:
                left = mid

        return left