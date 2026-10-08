class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        rows, cols = len(board), len(board[0])
        count = 0
        for row in range(rows):
            for col in range(cols):
                if (
                    board[row][col] == "X"
                    and (row == 0 or board[row - 1][col] != "X")
                    and (col == 0 or board[row][col - 1] != "X")
                ):
                    count += 1
        return count
