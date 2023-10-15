class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7
        goodNums = pow(20, n//2, mod)
        if n % 2:
            goodNums *= 5

        return goodNums % mod