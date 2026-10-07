class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        directions = ((0, 1), (1, 0))
        for r in range(rows):
            for c in range(cols):
                for dr, dc in directions:
                    before_r, before_c = r - dr, c - dc
                    if (
                        0 <= before_r < rows
                        and 0 <= before_c < cols
                        and board[before_r][before_c] != "#"
                    ):
                        continue
                    cells: list[str] = []
                    nr, nc = r, c
                    while 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":
                        cells.append(board[nr][nc])
                        nr += dr
                        nc += dc
                    if len(cells) != len(word):
                        continue
                    if all(
                        cell == " " or cell == letter
                        for cell, letter in zip(cells, word)
                    ):
                        return True
                    if all(
                        cell == " " or cell == letter
                        for cell, letter in zip(cells, reversed(word))
                    ):
                        return True
        return False
