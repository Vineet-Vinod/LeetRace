class Solution:
    def checkMove(
        self, board: list[list[str]], rMove: int, cMove: int, color: str
    ) -> bool:
        opponent = "W" if color == "B" else "B"
        for row_step in (-1, 0, 1):
            for col_step in (-1, 0, 1):
                if row_step == col_step == 0:
                    continue
                row, col = rMove + row_step, cMove + col_step
                if not (0 <= row < 8 and 0 <= col < 8) or board[row][col] != opponent:
                    continue
                row += row_step
                col += col_step
                while 0 <= row < 8 and 0 <= col < 8 and board[row][col] == opponent:
                    row += row_step
                    col += col_step
                if 0 <= row < 8 and 0 <= col < 8 and board[row][col] == color:
                    return True
        return False
