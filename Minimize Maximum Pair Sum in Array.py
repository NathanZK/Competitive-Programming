class Solution(object):
    def minPairSum(self, nums):
        nums = sorted(nums)
        start = 0
        end = len(nums) - 1
        mini = nums[0] + nums[1]
        while start < end:
            sum = nums[start] + nums[end]
            mini = max (mini, sum)
            start += 1
            end -= 1      
        return mini
