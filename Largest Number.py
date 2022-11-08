class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        n = len(nums)
        nums = [str(i) for i in nums]
        for i in range(n - 1):
            for j in range(n - 1 - i):
                if nums[j] + nums[j + 1] < nums[j + 1] + nums[j]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]

        return str(int("".join(nums)))
