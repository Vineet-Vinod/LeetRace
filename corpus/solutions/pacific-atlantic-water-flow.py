class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        def reachable(starts: List[Tuple[int, int]]) -> set[Tuple[int, int]]:
            seen = set(starts)
            queue = deque(starts)
            while queue:
                row, col = queue.popleft()
                for next_row, next_col in (
                    (row - 1, col),
                    (row + 1, col),
                    (row, col - 1),
                    (row, col + 1),
                ):
                    if (
                        0 <= next_row < rows
                        and 0 <= next_col < cols
                        and (next_row, next_col) not in seen
                        and heights[next_row][next_col] >= heights[row][col]
                    ):
                        seen.add((next_row, next_col))
                        queue.append((next_row, next_col))
            return seen

        pacific = reachable(
            [(row, 0) for row in range(rows)] + [(0, col) for col in range(cols)]
        )
        atlantic = reachable(
            [(row, cols - 1) for row in range(rows)]
            + [(rows - 1, col) for col in range(cols)]
        )
        return [[row, col] for row, col in sorted(pacific & atlantic)]
