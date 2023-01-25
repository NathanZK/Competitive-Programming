class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, int(c**0.5)
        while left <= right:
            squareSum = left ** 2 + right ** 2
            if squareSum == c:
                return True
            elif squareSum > c:
                right -= 1
            else:
                left += 1

        return False
