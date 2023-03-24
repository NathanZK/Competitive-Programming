class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates = []

        for i in range(len(nums)):
            while nums[i] != i + 1 and nums[i] != -1:
                idx = nums[i] - 1
                if nums[i] == nums[idx]:
                    duplicates.append(nums[i])
                    nums[i] = -1

                nums[idx], nums[i] = nums[i], nums[idx]

        return duplicates
