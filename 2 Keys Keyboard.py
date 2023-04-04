class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0

        primes = self.primes(n)
        ops = 0

        i = 0
        while n != 1: 
            while i < len(primes) and n % primes[i] == 0:
                ops += (primes[i]-1)
                ops += 1
                n //= primes[i]

            i += 1

        return ops

    def primes(self, n):
        if n < 2:
            return [False, False]

        isPrime = [True for _ in range(n+1)]
        isPrime[0] = isPrime[1] = False

        i = 2
        while i*i <= n:
            if isPrime[i]:
                j = i * i
                while j <= n:
                    isPrime[j] = False
                    j += i

            i += 1

        return [i for i in range(len(isPrime)) if isPrime[i] == True]
