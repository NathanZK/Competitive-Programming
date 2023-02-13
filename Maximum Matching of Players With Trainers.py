class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        p1, p2 = 0, 0
        count = 0
        while p1 < len(players) and p2 < len(trainers):
            if trainers[p2] >= players[p1]:
                p1 += 1
                count += 1
            p2 += 1

        return count
