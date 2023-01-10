class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        fir = (num - 3)/3
        if int(fir) != fir:
            return []
        fir = int(fir)
        return [fir, fir + 1, fir + 2]
