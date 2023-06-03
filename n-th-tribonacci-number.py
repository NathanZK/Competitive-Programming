class Solution:
    def __init__(self):
        self.memo = {}

    def tribonacci(self, n: int) -> int:
        return self.dp(n)

    def dp(self, n):
        if n in self.memo:
            return self.memo[n]

        if n == 0:
            return 0
        if n <= 2:
            return 1

        self.memo[n] = self.dp(n-1)+self.dp(n-2)+self.dp(n-3)
        return self.memo[n]