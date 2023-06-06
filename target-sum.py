class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def dp(index, currSum):
            if index == len(nums):
                if currSum == target:
                    return 1
                else:
                    return 0

            state = (index, currSum)
            if state in memo:
                return memo[state]

            memo[state] = dp(index+1, currSum + nums[index]) + dp(index+1, currSum - nums[index])
            return memo[state]

        return dp(0, 0)