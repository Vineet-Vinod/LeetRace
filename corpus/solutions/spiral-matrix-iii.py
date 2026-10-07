class Solution:
    def spiralMatrixIII(
        self, rows: int, cols: int, rStart: int, cStart: int
    ) -> List[List[int]]:
        out = []
        r, c = rStart, cStart
        steps = 1
        if 0 <= r < rows and 0 <= c < cols:
            out.append([r, c])
        while len(out) < rows * cols:
            for dr, dc, count in (
                (0, 1, steps),
                (1, 0, steps),
                (0, -1, steps + 1),
                (-1, 0, steps + 1),
            ):
                for _ in range(count):
                    r += dr
                    c += dc
                    if 0 <= r < rows and 0 <= c < cols:
                        out.append([r, c])
            steps += 2
        return out
