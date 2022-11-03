class Solution(object):
    def myPow(self, x, n):
        if n < 0:
            return 1 / self.myPow(x, abs(n))     
        elif n == 0:
            return 1.0
        elif n % 2 == 1:
            return self.myPow(x, n - 1) * x
        elif n % 2 == 0:
            return self.myPow(x * x, n // 2)
