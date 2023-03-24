class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        for i in range(len(nums)):
            while nums[i] != i + 1 and nums[i] != -1:
                idx = nums[i] - 1
                if nums[idx] == nums[i]:
                    nums[i] = -1
                else:
                    nums[i], nums[idx] = nums[idx], nums[i]
        
        missing = []
        for i, num in enumerate(nums):
            if num == -1:
                missing.append(i + 1)

        return missing
