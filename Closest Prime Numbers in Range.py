class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        primes = self.generatePrimes(right)
        pairs = []
        
        for i in range(left, right+1):
            if primes[i]:
                pairs.append(i)

        if len(pairs) < 2:
            return [-1,-1]

        minPair = pairs[:2]
        minDiff = float('inf')

        for i in range(len(pairs)-1):
            if pairs[i+1] - pairs[i] < minDiff:
                minDiff = pairs[i+1] - pairs[i]
                minPair = [pairs[i], pairs[i+1]]
                    
        return minPair

    def generatePrimes(self, n):
        if n < 2:
            return [False, False]

        isPrime = [True for _ in range(n+1)]
        isPrime[0] = isPrime[1] = False

        i = 2
        while i * i <= n:
            if isPrime[i]:
                j = i * i
                while j <= n:
                    isPrime[j] = False
                    j += i
            
            i += 1

        return isPrime
