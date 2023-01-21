class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sortedNums = sorted(nums)
        indNums = {}
        for i, n in enumerate(sortedNums):
            if n not in indNums:
                indNums[n] = i

        smaller = []
        for n in nums:
            smaller.append(indNums[n])

        return smaller

            
        
