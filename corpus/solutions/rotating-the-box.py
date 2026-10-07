class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        rows = [row[:] for row in boxGrid]
        for row in rows:
            write = len(row) - 1
            for col in range(len(row) - 1, -1, -1):
                if row[col] == "*":
                    write = col - 1
                elif row[col] == "#":
                    row[col], row[write] = ".", "#"
                    write -= 1
        return [
            [rows[r][c] for r in range(len(rows) - 1, -1, -1)]
            for c in range(len(rows[0]))
        ]
