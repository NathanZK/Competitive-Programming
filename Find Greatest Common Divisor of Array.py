class Solution:
    def findGCD(self, nums: List[int]) -> int:
        min_, max_ = min(nums), max(nums)

        def gcd(a, b):
            if b == 0:
                return a

            return gcd(b, a%b)

        return gcd(min_, max_)
