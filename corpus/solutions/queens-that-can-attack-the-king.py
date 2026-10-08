class Solution:
    def queensAttacktheKing(
        self, queens: List[List[int]], king: List[int]
    ) -> List[List[int]]:
        occupied = {tuple(position) for position in queens}
        attacking = []
        for row_step in (-1, 0, 1):
            for column_step in (-1, 0, 1):
                if row_step == 0 and column_step == 0:
                    continue
                row, column = king
                while 0 <= row + row_step < 8 and 0 <= column + column_step < 8:
                    row += row_step
                    column += column_step
                    if (row, column) in occupied:
                        attacking.append([row, column])
                        break
        return sorted(attacking)
