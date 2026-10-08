class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        rows, columns = len(land), len(land[0])
        groups = []
        for row in range(rows):
            for column in range(columns):
                if land[row][column] == 0:
                    continue
                bottom = row
                while bottom + 1 < rows and land[bottom + 1][column] == 1:
                    bottom += 1
                right = column
                while right + 1 < columns and land[row][right + 1] == 1:
                    right += 1
                groups.append([row, column, bottom, right])
                for r in range(row, bottom + 1):
                    for c in range(column, right + 1):
                        land[r][c] = 0
        return groups
