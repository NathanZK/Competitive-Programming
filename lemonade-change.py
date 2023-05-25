class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        countChange = Counter()

        for bill in bills:
            if bill == 5:
                countChange[5] += 1
            elif bill == 10 and countChange[5] >= 1:
                countChange[10] += 1
                countChange[5] -= 1
            elif bill == 20:
                if countChange[10] >= 1 and countChange[5] >= 1:
                    countChange[10] -= 1
                    countChange[5] -= 1
                elif countChange[5] >= 3:
                    countChange[5] -= 3
                else:
                    return False
            else:
                return False

        return True