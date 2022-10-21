class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalsum = 0
        leftsum = 0
        for i in nums:
            totalsum += i
        for i in range(len(nums)):
            rightsum = totalsum - nums[i] - leftsum
            if leftsum == rightsum:
                return i
            leftsum += nums[i]
            
        return -1
