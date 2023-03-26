class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        repLoss = []

        for i in range(len(nums)):
            while nums[i] != i + 1 and nums[i] != -1:
                idx = nums[i]-1
                if nums[i] == nums[idx]:
                    repLoss.append(nums[i])
                    nums[i] = -1
                else:
                    nums[idx], nums[i] = nums[i], nums[idx]
        
        for i in range(len(nums)):
            if nums[i] == -1:
                repLoss.append(i+1)

        return repLoss
