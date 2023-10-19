class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        dp = {}
        totalSum = sum(nums)
        if totalSum % 2 == 1:
            return False

        targetSum = totalSum//2

        def dfs(index, currSum):
            if currSum == targetSum:
                return True

            if currSum > targetSum or index == len(nums):
                return False

            if (index, currSum) not in dp:
                select = dfs(index+1, currSum+nums[index])
                avoid = dfs(index+1, currSum)
                dp[(index, currSum)] = select or avoid

            return dp[(index, currSum)]

        return dfs(0, 0)