class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        columns = len(obstacleGrid[0])
        paths = [0] * columns
        paths[0] = 1
        for row in obstacleGrid:
            for col, cell in enumerate(row):
                if cell == 1:
                    paths[col] = 0
                elif col > 0:
                    paths[col] += paths[col - 1]
        return paths[-1]
