class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        dp = [0] * (amount+1)

        for i in range(1, amount+1):
            minCoins = float('inf')
            j = 0

            while j < len(coins) and i - coins[j] >= 0:
                minCoins = min(minCoins, dp[i-coins[j]])
                j += 1
            dp[i] = minCoins + 1

        return dp[amount] if dp[amount] != float('inf') else -1