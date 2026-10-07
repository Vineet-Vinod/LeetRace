class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        x_count = sum(row.count("X") for row in board)
        o_count = sum(row.count("O") for row in board)
        if x_count not in (o_count, o_count + 1):
            return False
        lines = list(board) + ["".join(board[r][c] for r in range(3)) for c in range(3)]
        lines += [
            "".join(board[i][i] for i in range(3)),
            "".join(board[i][2 - i] for i in range(3)),
        ]
        x_wins = any(line == "XXX" for line in lines)
        o_wins = any(line == "OOO" for line in lines)
        if x_wins and o_wins:
            return False
        if x_wins and x_count != o_count + 1:
            return False
        if o_wins and x_count != o_count:
            return False
        return True
