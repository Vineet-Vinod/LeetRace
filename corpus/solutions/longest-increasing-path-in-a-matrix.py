from collections import deque


class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        degree = [[0] * n for _ in range(m)]
        queue = deque()
        for i in range(m):
            for j in range(n):
                degree[i][j] = sum(
                    0 <= x < m and 0 <= y < n and matrix[x][y] < matrix[i][j]
                    for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1))
                )
                if degree[i][j] == 0:
                    queue.append((i, j))
        answer = 0
        while queue:
            answer += 1
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                        degree[x][y] -= 1
                        if degree[x][y] == 0:
                            queue.append((x, y))
        return answer
