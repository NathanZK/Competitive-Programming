class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        countColors = Counter()
        minRabbits = 0

        for ans in answers:
            if countColors[ans] == 0:
                minRabbits += (ans+1)
                countColors[ans] = ans
            else:
                countColors[ans] -= 1

        return minRabbits