class Solution:
    def countCornerRectangles(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        seen_pairs = Counter()
        answer = 0
        for row in range(rows):
            ones = [col for col in range(columns) if grid[row][col] == 1]
            for i, left in enumerate(ones):
                for right in ones[i + 1 :]:
                    answer += seen_pairs[(left, right)]
                    seen_pairs[(left, right)] += 1
        return answer
