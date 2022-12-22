class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numList = set()
        for i in range(len(nums)):
            numList.add(i)

        for num in nums:
            if num in numList:
                numList.remove(num)

        if len(numList) != 0:
            return list(numList)[0]
        return len(nums)
