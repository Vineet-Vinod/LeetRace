class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        answer = []
        for start in range(n):
            col = start
            for row in range(m):
                nxt = col + grid[row][col]
                if nxt < 0 or nxt >= n or grid[row][nxt] != grid[row][col]:
                    col = -1
                    break
                col = nxt
            answer.append(col)
        return answer
