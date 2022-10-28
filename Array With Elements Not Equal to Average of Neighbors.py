class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        print(nums)
        i = 1
        while i < n - 1:
            if nums[i] == (nums[i-1] + nums[i+1]) / 2:
                nums[i+1], nums[(i+2) % n] =  nums[(i+2) % n], nums[i+1]
            if nums[i] == (nums[i-1] + nums[i+1]) / 2:
                nums[i], nums[i+1] =  nums[i+1], nums[i]
            i += 1
        return nums
