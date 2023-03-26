class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        for i in range(len(nums)):
            while nums[i] != i + 1 and nums[i] > 0:
                idx = nums[i] - 1
                if nums[i] > len(nums) or nums[idx] == nums[i]:
                    nums[i] = -1
                else:
                    nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
        
        for i in range(len(nums)):
            if nums[i] <= 0:
                return i + 1

        return len(nums) + 1
