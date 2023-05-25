class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return 0

        nums.sort() 
        minDiff = float('inf')
        for i in range(4):
            minDiff = min(minDiff, nums[i-4] - nums[i])

        return minDiff