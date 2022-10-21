class Solution(object):
    def sortColors(self, nums):
        start, value, end = 0, 0, len(nums) - 1
        while value <= end:
            if nums[value] == 0:
                nums[value], nums[start] = nums[start], nums[value]
                start += 1
            elif nums[value] == 2:
                nums[value], nums[end] = nums[end], nums[value]
                end -= 1
                continue
            value += 1
        return nums
