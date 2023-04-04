class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        numSub = 0

        for i in range(len(nums)):
            currGcd = nums[i]

            for j in range(i, len(nums)):
                currGcd = self.gcd(currGcd, nums[j])
                if currGcd == k:
                    numSub += 1
                elif currGcd % k != 0 or currGcd < k:
                    break

        return numSub

    def gcd(self, a, b):
        if b == 0:
            return a

        return self.gcd(b, a%b)
