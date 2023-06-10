class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}

        def backtrack(index, currSum):
            if currSum >= target:
                return 1 if currSum == target else 0

            if index >= len(nums):
                return 0

            if currSum in memo:
                return memo[currSum]

            totalSum = 0
            for i in range(len(nums)):
                totalSum += backtrack(i, currSum + nums[i])

            memo[currSum] = totalSum
            return memo[currSum]

        return backtrack(0, 0)