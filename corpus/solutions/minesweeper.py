class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        rows, cols = len(board), len(board[0])
        r, c = click
        if board[r][c] == "M":
            board[r][c] = "X"
            return board
        queue = deque([(r, c)])
        while queue:
            r, c = queue.popleft()
            if board[r][c] != "E":
                continue
            adjacent = [
                (nr, nc)
                for nr in range(max(0, r - 1), min(rows, r + 2))
                for nc in range(max(0, c - 1), min(cols, c + 2))
                if (nr, nc) != (r, c)
            ]
            mines = sum(board[nr][nc] == "M" for nr, nc in adjacent)
            if mines:
                board[r][c] = str(mines)
            else:
                board[r][c] = "B"
                queue.extend((nr, nc) for nr, nc in adjacent if board[nr][nc] == "E")
        return board
