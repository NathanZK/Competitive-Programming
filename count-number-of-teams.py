class Solution:
    def numTeams(self, rating: List[int]) -> int:
        lesserCount = [0 for _ in range(len(rating))]
        greaterCount = [0 for _ in range(len(rating))]
        pathCount = 0

        for i in range(len(rating)):
            for j in range(i+1, len(rating)):
                src, des = rating[i], rating[j]
                if src < des:
                    lesserCount[i] += 1
                if src > des:
                    greaterCount[i] += 1

        for i in range(len(rating)):
            for j in range(i+1, len(rating)):
                src, des = rating[i], rating[j]

                if src < des:
                    pathCount += lesserCount[j]
                if src > des:
                    pathCount += greaterCount[j]

        return pathCount