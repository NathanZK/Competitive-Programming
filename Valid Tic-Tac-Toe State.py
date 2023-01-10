class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        flatten = "".join(board)
        countXO = Counter(flatten)
        if countXO['X'] < countXO['O'] or countXO['X'] > countXO['O'] + 1:
            return False

        xWins = False
        oWins = False
        for row in board:
            if row == "XXX":
                xWins = True
            elif row == "OOO":
                oWins = True

        for i in range(3):
            col = []
            for j in range(3):
                col.append(board[j][i])
            col = "".join(col)
            if col == "XXX":
                xWins = True
            elif col == "OOO":
                oWins = True

        dig1 = board[0][0] + board[1][1] + board[2][2]
        dig2 = board[0][2] + board[1][1] + board[2][0]
        if dig1 == "XXX" or dig2 == "XXX":
            xWins = True
        elif dig1 == "OOO" or dig2 == "OOO":
            oWins = True

        if xWins and oWins:
            return False
        elif  (xWins and countXO['X'] == countXO['O']) or (oWins and countXO['O'] < countXO['X']):
            return False

        return True
