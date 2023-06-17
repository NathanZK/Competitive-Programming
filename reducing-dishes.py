class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse = True)
        if satisfaction[0] <= 0:
            return 0

        maxLikeTime = 0
        for i in range(len(satisfaction)):
            likeTime = 0
            for j in range(i+1):
                likeTime += (satisfaction[j]*(i-j+1))

            if likeTime > maxLikeTime:
                maxLikeTime = likeTime
            else:
                return maxLikeTime

        return maxLikeTime