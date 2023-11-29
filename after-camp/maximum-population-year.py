class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        years = [0] * 101

        for birth, death in logs:
            years[birth-1950] += 1
            years[death-1950] -= 1

        maxYear, numPopulation = 0, years[0]
        for i in range(1, len(years)):
            years[i] += years[i-1]

            if years[i] > numPopulation:
                maxYear = i
                numPopulation = years[i]

        return maxYear + 1950

        
        