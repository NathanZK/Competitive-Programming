class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        currSum = 0
        prefixSum = {0 : 1}
        sumK = 0
        for i in nums:
            currSum += i
            diff = currSum - k
            
            sumK += prefixSum.get(diff, 0)
            prefixSum[currSum] = 1 + prefixSum.get(currSum, 0)

        return sumK
            
            
        
