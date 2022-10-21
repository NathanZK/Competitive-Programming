class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        num = len(nums) - k
        nums[:] = nums[num:] + nums[:num]
