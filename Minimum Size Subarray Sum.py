class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if nums[0] >= target:
            return 1
        found = False
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i - 1]
            if nums[i] >= target and not found:
                next = i
                found = True
        if nums[-1] < target:
            return 0
        
        left = 0
        minLength = next + 1
        length = minLength
        while next < len(nums):
            value = nums[next] - nums[left]
            if value >= target:
                length -= 1
                left += 1
            else:
                length += 1
                next += 1
            minLength = min(minLength, length)
        return minLength
