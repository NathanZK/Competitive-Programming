class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = 0
        orgLen = len(nums)
        left, right = 0, len(nums) - 1
        while left < right:
            sum = nums[left] + nums[right]
            if sum > k:
                right -= 1
            elif sum < k:
                left += 1
            else:
                left += 1
                right -= 1
                count += 1
                
        return count
