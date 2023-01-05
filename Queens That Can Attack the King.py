class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        attKing = [[] for i in range(8)]
        xKing, yKing = king
        for xQueen, yQueen in queens:
            if xQueen == xKing:
                self.helper(xQueen, yQueen, yQueen, yKing, 0, 1, attKing)
            elif yQueen == yKing:
                self.helper(xQueen, yQueen, xQueen, xKing, 2, 0, attKing)
            elif abs(xQueen - xKing) == abs(yQueen - yKing):
                if yQueen > yKing:
                    self.helper(xQueen, yQueen, xQueen, xKing, 4, 0, attKing)
                elif yQueen < yKing:
                    self.helper(xQueen, yQueen, xQueen, xKing, 6, 0, attKing)

        attackKing = []
        for att in attKing:
            if att != []:
                attackKing.append(att)

        return attackKing

    def helper(self, xQueen, yQueen, lQueen, lKing, indX, indY, attKing):

        if lQueen > lKing and (attKing[indX] == [] or lQueen < attKing[indX][indY]):
            attKing[indX] = [xQueen, yQueen]
        elif lQueen < lKing and (attKing[indX + 1] == [] or lQueen > attKing[indX + 1][indY]):
            attKing[indX + 1] = [xQueen, yQueen]

