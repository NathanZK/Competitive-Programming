class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        newList = sorted(zip(ages, scores))

        n = len(newList)
        dp = [0] * n

        for i in range(n):
            dp[i] = newList[i][1]

            for j in range(i):
                if newList[j][1] <= newList[i][1]:
                    dp[i] = max(dp[i], dp[j] + newList[i][1])

        return max(dp)