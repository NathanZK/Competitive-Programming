class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        l, r = len(nums) - 3, len(nums) - 1
        while l >= 0:
            if nums[l] + nums[l + 1] > nums[r]:
                return nums[l] + nums[l + 1] + nums[r]
            l -= 1
            r -= 1
            
        return 0
            
