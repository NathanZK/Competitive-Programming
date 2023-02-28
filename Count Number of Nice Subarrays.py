class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        evens = []
        count = 1
        for n in nums:
            if n % 2 == 1:
                evens.append(count)
                count = 1
            else:
                count += 1
        evens.append(count)

        odds = 0
        for i in range(len(evens) - k):
            odds += evens[i] * evens[i+k]

        return odds
