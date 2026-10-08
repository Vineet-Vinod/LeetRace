class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        top_remaining = sum(grid[0])
        bottom_collected = 0
        answer = float("inf")
        for col in range(len(grid[0])):
            top_remaining -= grid[0][col]
            answer = min(answer, max(top_remaining, bottom_collected))
            bottom_collected += grid[1][col]
        return answer
