class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        for i in range(len(nums)):
            while nums[i] != i+1:
                idx = nums[i] - 1
                if nums[idx] == nums[i]:
                    return nums[i]

                nums[idx], nums[i] = nums[i], nums[idx]
