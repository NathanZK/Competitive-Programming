class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        dist = float("inf")
        index = -1
        for ind, cor in enumerate(points):
            manDist = abs(cor[0] - x) + abs(cor[1] - y)
            if (cor[0] == x or cor[1] == y) and manDist < dist:
                index = ind
                dist = manDist

        return index
