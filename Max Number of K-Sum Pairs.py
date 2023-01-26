class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, right = 0, len(nums) - 1
        maxOps = 0
        while left < right:
            Sum = nums[left] + nums[right]
            if k == Sum:
                maxOps += 1
                left += 1
                right -= 1
            elif k < Sum:
                right -= 1
            else:
                left += 1

        return maxOps
