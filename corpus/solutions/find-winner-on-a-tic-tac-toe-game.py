class Solution:
    def tictactoe(self, moves: list[list[int]]) -> str:
        board = [["" for _ in range(3)] for _ in range(3)]
        for index, (row, column) in enumerate(moves):
            board[row][column] = "A" if index % 2 == 0 else "B"
        lines = board + [
            [board[row][column] for row in range(3)] for column in range(3)
        ]
        lines.extend(
            [[board[i][i] for i in range(3)], [board[i][2 - i] for i in range(3)]]
        )
        for line in lines:
            if line[0] and line.count(line[0]) == 3:
                return line[0]
        return "Draw" if len(moves) == 9 else "Pending"
