class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        score = 0
        for card in cardPoints[0:k]:
            score += card
        if k == n:
            return score
        maxScore = score
        left , right = k - 1, n - 1
        while left >= 0:
            score -= cardPoints[left]
            score += cardPoints[right]
            left -= 1
            right -= 1
            maxScore = max(maxScore, score)
        return maxScore
