class Solution:
    def minCost(
        self,
        startPos: List[int],
        homePos: List[int],
        rowCosts: List[int],
        colCosts: List[int],
    ) -> int:
        start_row, start_col = startPos
        home_row, home_col = homePos
        row_step = 1 if home_row > start_row else -1
        col_step = 1 if home_col > start_col else -1
        total = 0
        row = start_row
        while row != home_row:
            row += row_step
            total += rowCosts[row]
        col = start_col
        while col != home_col:
            col += col_step
            total += colCosts[col]
        return total
