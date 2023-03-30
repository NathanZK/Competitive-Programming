class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        distance = x ^ y
        count = 0

        while distance > 0:
            count += (distance&1)
            distance >>=1

        return count
