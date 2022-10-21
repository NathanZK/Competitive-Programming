class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums = [int(i) for i in nums]
        nums = sorted(nums, reverse = True)
        return str(nums[k - 1])
