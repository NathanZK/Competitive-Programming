class Solution:
    def minSteps(self, n: int) -> int:
        dp = {1:0}

        for i in range(2, n+1):
            minVal = i
            for j in range(i//2, 0, -1):
                if i % j == 0:
                    minVal = i//j + dp[j]
                    break
            
            dp[i] = minVal

        return dp[n]