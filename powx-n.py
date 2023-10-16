class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            return 1 / (self.myPow(x, abs(n)))
        if n % 2 == 1:
            return x * self.myPow(x, n - 1)

        root = self.myPow(x, n // 2)
        return root * root