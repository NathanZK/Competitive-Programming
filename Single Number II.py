class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        mask = 1
        single = 0

        while mask < 2**32:
            count = 0
            for num in nums:
                count += (num&mask)

            if count % 3 != 0:
                single |= mask

            mask <<= 1

        if single & (1<< 31):
            return (2 ** 32 - single) * -1

        return single
