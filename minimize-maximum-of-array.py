class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]

        for i in range(len(nums)):
            nums[i] = ceil(nums[i]/(i+1))

        return max(nums)