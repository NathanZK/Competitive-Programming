class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[0] * (len(s)+1) for i in range(len(s)+1)]
        longestSubsequence = 0

        for left in range(len(s)):
            for right in range(len(s)-1, left - 1, -1):
                if s[left] == s[right]:
                    dp[left][right] = 1 if left == right else 2
                    if left - 1 >= 0:
                        dp[left][right] += dp[left-1][right+1]
                else:
                    dp[left][right] = dp[left][right+1]
                    if left - 1 >= 0:
                        dp[left][right] = max(dp[left][right], dp[left-1][right])

                longestSubsequence = max(longestSubsequence, dp[left][right])

        return longestSubsequence