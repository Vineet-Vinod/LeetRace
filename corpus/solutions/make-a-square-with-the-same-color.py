class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        for row in range(2):
            for col in range(2):
                black = sum(
                    grid[r][c] == "B" for r in (row, row + 1) for c in (col, col + 1)
                )
                if black != 2:
                    return True
        return False
