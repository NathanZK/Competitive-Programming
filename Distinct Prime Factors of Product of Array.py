class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        distinct = set()

        for num in nums:
            self.distinctPrimes(num, distinct)

        return len(distinct)

    def distinctPrimes(self, num, distinct):
        d = 2
        count = 0

        while d * d <= num:
            if num % d == 0:
                distinct.add(d)

            while num%d == 0:
                num //= d
            
            d += 1

        if num > 1:
            distinct.add(num)
