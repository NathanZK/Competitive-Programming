class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times

        countVote = {}
        self.winner = {}
        previousWinner = -1

        for i, p in enumerate(persons):            
            countVote[p] = countVote.get(p, 0) + 1

            if countVote[p] >= countVote.get(previousWinner, 0):
                self.winner[i] = p
                previousWinner = p
            else:
                self.winner[i] = previousWinner

    def q(self, t: int) -> int:

        left, right = -1, len(self.times)
        while left + 1 < right:
            mid = (left + right)//2
            if self.times[mid] <= t:
                left = mid
            else:
                right = mid

        return self.winner[left]
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
