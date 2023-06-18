class Solution:
    def candy(self, ratings: List[int]) -> int:
        leftCandies = [1] * len(ratings)
        rightCandies = [1]* len(ratings)

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                leftCandies[i] = leftCandies[i-1] + 1

        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                rightCandies[i] = rightCandies[i+1] + 1

        totalCandies = 0
        for i in range(len(ratings)):
            totalCandies += max(leftCandies[i],rightCandies[i])

        return totalCandies