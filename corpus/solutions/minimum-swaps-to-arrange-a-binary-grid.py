class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        trailing = []
        for row in grid:
            count = 0
            for value in reversed(row):
                if value:
                    break
                count += 1
            trailing.append(count)
        swaps = 0
        for row in range(n):
            needed = n - row - 1
            index = next((i for i in range(row, n) if trailing[i] >= needed), -1)
            if index == -1:
                return -1
            swaps += index - row
            while index > row:
                trailing[index], trailing[index - 1] = (
                    trailing[index - 1],
                    trailing[index],
                )
                index -= 1
        return swaps
