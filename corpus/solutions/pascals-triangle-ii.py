class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for _ in range(rowIndex):
            row = (
                [1]
                + [row[index - 1] + row[index] for index in range(1, len(row))]
                + [1]
            )
        return row
