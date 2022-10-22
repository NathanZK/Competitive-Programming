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

        if k > len(evens) - 1:
            return 0
        i = 0
        odds = 0
        while k + i < len(evens):
            odds += evens[k + i] * evens[i]
            i += 1
        return odds
