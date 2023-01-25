class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        self.reverse(0, len(nums)-1, nums)
        self.reverse(0, k-1, nums)
        self.reverse(k, len(nums)-1, nums)

    def reverse(self, left, right, nums):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
