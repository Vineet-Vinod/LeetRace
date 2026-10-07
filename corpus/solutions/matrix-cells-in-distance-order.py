class Solution:
    def allCellsDistOrder(
        self, rows: int, cols: int, rCenter: int, cCenter: int
    ) -> List[List[int]]:
        cells = [[row, col] for row in range(rows) for col in range(cols)]
        cells.sort(
            key=lambda cell: (
                abs(cell[0] - rCenter) + abs(cell[1] - cCenter),
                cell[0],
                cell[1],
            )
        )
        return cells
