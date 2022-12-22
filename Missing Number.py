class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numList = {}
        for i in range(len(nums)):
            numList[i] = 1

        for num in nums:
            if num in numList:
                del numList[num]

        val = list(numList.keys())
        if len(val) == 1:
            return val[0]

        return len(nums)
        
