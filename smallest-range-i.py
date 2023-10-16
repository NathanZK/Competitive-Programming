class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        smallestRange = max(0, max(nums)-min(nums)-2*k)

        return smallestRange