class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        leftMin = [nums[0]] * len(nums)
        rightMax = [nums[-1]] * len(nums)

        for i in range(1, len(nums)):        
            if nums[i] < leftMin[i-1]:
                leftMin[i] = nums[i]
            else:
                leftMin[i] = leftMin[i-1]

        for i in range(len(nums)-2, -1, -1):
            if nums[i] > rightMax[i+1]:
                rightMax[i] = nums[i]
            else:
                rightMax[i] = rightMax[i+1]

        for i in range(1, len(nums)-1):
            if leftMin[i] < nums[i] < rightMax[i]:
                return True


        return False