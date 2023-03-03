class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefixSum = {0: 1}
        runningSum, nonEmpty = 0, 0

        for n in nums:
            runningSum += n
            diff = runningSum - goal

            nonEmpty += prefixSum.get(diff, 0)
            prefixSum[runningSum] = prefixSum.get(runningSum, 0) + 1

        return nonEmpty

