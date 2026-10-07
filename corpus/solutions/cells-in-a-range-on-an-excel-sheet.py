class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        start_col, start_row = ord(s[0]), int(s[1])
        end_col, end_row = ord(s[3]), int(s[4])
        return [
            chr(col) + str(row)
            for col in range(start_col, end_col + 1)
            for row in range(start_row, end_row + 1)
        ]
