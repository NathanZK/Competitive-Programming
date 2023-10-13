class Solution:
    def countOrders(self, n: int) -> int:
        mod = 10**9 + 7
        currPow = 2**n
        permutation = self.factorial(2*n)
        res = permutation//currPow

        return res % mod
    
    def factorial(self, n):
        total = 1

        while n > 0:
            total *= n
            n -= 1

        return total