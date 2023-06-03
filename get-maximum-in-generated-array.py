class Solution:
    def __init__(self):
        self.memo = {0: 0, 1: 1}

    def getMaximumGenerated(self, n: int) -> int:
        if n <= 1:
            return n

        for i in range(n+1):
            self.dp(i)

        return max(self.memo.values())

    def dp(self, n):
        if n in self.memo:
            return self.memo[n]

        self.memo[n] = self.dp(n//2)
        if n%2 == 1:
            self.memo[n] += self.dp(n//2 + 1)

        return self.memo[n]