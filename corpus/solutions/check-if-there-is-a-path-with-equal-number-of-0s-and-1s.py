class Solution:
    def isThereAPath(self, grid: List[List[int]]) -> bool:
        rows, cols = len(grid), len(grid[0])
        path_length = rows + cols - 1
        if path_length % 2:
            return False
        reachable = [[set() for _ in range(cols)] for _ in range(rows)]
        reachable[0][0].add(grid[0][0])
        for row in range(rows):
            for col in range(cols):
                if row == 0 and col == 0:
                    continue
                previous = set()
                if row:
                    previous.update(reachable[row - 1][col])
                if col:
                    previous.update(reachable[row][col - 1])
                reachable[row][col] = {ones + grid[row][col] for ones in previous}
        return path_length // 2 in reachable[-1][-1]
