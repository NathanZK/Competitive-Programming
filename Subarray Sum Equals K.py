class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum = 0
        prefixSum = {0 : 1}
        res = 0
        for i in nums:
            sum += i
            diff = sum - k
            
            res += prefixSum.get(diff, 0)
            prefixSum[sum] = 1 + prefixSum.get(sum, 0)
            
        return res
