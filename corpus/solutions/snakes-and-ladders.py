class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        target = n * n

        def cell(label: int) -> int:
            q, r = divmod(label - 1, n)
            row = n - 1 - q
            col = r if q % 2 == 0 else n - 1 - r
            return board[row][col]

        dist = [-1] * (target + 1)
        dist[1] = 0
        q = deque([1])
        while q:
            x = q.popleft()
            if x == target:
                return dist[x]
            for y in range(x + 1, min(x + 6, target) + 1):
                z = cell(y)
                z = y if z == -1 else z
                if dist[z] < 0:
                    dist[z] = dist[x] + 1
                    q.append(z)
        return -1
