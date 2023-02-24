class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        currSum = 0
        prefixSum = {0:1}
        divK = 0
        for num in nums:
            currSum += num
            rem = currSum % k

            divK += prefixSum.get(rem,0)
            prefixSum[rem] = 1 + prefixSum.get(rem, 0)

        return divK




    
