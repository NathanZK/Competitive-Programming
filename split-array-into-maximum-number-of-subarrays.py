class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        initial = 2**32 -1
        for i in range(len(nums)):
            initial &= nums[i]

        if initial > 0:
            return 1

        initial = 2**32 -1
        count = 0
        for i in range(len(nums)):
            initial &= nums[i]
            if initial == 0:
                count += 1
                initial = 2**32 -1

        return count