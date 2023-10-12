class Solution:
    def minOperations(self, nums: List[int]) -> int:
        diff = len(nums) - 1
        nums.sort()
        minOps = float('inf')
        duplicates = [0] * (len(nums))
        duplicateNums = 0

        numSet = set()
        for i in range(len(nums)):
            if nums[i] in numSet:
                duplicateNums += 1
            
            duplicates[i] = duplicateNums
            numSet.add(nums[i])

        for i in range(len(nums)):
            target = nums[i] + diff
            right = self.binarySearch(target, nums)

            currOps = i + (len(nums)-right) + (duplicates[right-1]-duplicates[i])
            if currOps < minOps:
                minOps = currOps

        return minOps

    def binarySearch(self, target, nums):
        left, right = -1, len(nums)

        while left + 1 < right:
            mid = (left + right)//2

            if nums[mid] > target:
                right = mid

            else:
                left = mid

        return right