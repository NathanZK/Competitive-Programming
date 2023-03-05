class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left, right = 0, max(nums) + 1

        while left + 1 < right:
            mid = (left + right)//2
            if self.divSum(nums, mid) > threshold:
                left = mid
            else:
                right = mid

        return right

    def divSum(self, nums, divisor):
        totalSum = 0

        for n in nums:
            totalSum += (math.ceil(n/divisor))

        return totalSum
