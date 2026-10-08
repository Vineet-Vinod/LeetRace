class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        rows, cols = len(picture), len(picture[0])
        row_counts = [sum(cell == "B" for cell in row) for row in picture]
        col_counts = [
            sum(picture[r][c] == "B" for r in range(rows)) for c in range(cols)
        ]
        return sum(
            picture[r][c] == "B" and row_counts[r] == 1 and col_counts[c] == 1
            for r in range(rows)
            for c in range(cols)
        )
