class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows, columns = len(grid2), len(grid2[0])
        seen = set()
        answer = 0
        for row in range(rows):
            for column in range(columns):
                if grid2[row][column] == 0 or (row, column) in seen:
                    continue
                stack = [(row, column)]
                seen.add((row, column))
                is_sub_island = True
                while stack:
                    current_row, current_column = stack.pop()
                    if grid1[current_row][current_column] == 0:
                        is_sub_island = False
                    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nr, nc = current_row + dr, current_column + dc
                        if (
                            0 <= nr < rows
                            and 0 <= nc < columns
                            and grid2[nr][nc] == 1
                            and (nr, nc) not in seen
                        ):
                            seen.add((nr, nc))
                            stack.append((nr, nc))
                answer += is_sub_island
        return answer
