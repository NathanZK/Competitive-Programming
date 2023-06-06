class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)
            
        return max(self.rob1(nums[:len(nums)-1]), self.rob1(nums[1:]))
    
    def rob1(self, nums: List[int]) -> int:
        nums.append(0)

        for i in range(1, len(nums)-1):
            nums[i] = max(nums[i] + nums[i-2], nums[i-1])

        return nums[-2]