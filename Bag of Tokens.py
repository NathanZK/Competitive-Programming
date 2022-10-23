class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        score = 0
        maxScore = 0
        left, right = 0, len(tokens) - 1
        while left <= right:
            if power >= tokens[left]:
                power -= tokens[left]
                score += 1
                left += 1
            elif power < tokens[left] and score > 0 and left < right:
                power += tokens[right]
                score -= 1
                right -= 1
            else:
                return maxScore
            maxScore = max(maxScore, score)
 
        return maxScore
