class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLength, currSum = float('inf'), 0
        left = 0
        for right in range(len(nums)):
            currSum += nums[right]
            while currSum >= target:
                minLength = min(minLength, right - left + 1)
                currSum -= nums[left]
                left += 1

        if minLength == float('inf'):
            return 0

        return minLength
            
