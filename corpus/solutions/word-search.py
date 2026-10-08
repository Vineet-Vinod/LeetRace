class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        if len(word) > rows * cols:
            return False
        available = Counter(char for row in board for char in row)
        needed = Counter(word)
        if any(count > available[char] for char, count in needed.items()):
            return False
        if available[word[0]] > available[word[-1]]:
            word = word[::-1]

        def search(row: int, col: int, index: int) -> bool:
            if board[row][col] != word[index]:
                return False
            if index == len(word) - 1:
                return True
            char = board[row][col]
            board[row][col] = "\0"
            found = (
                (
                    row > 0
                    and board[row - 1][col] != "\0"
                    and search(row - 1, col, index + 1)
                )
                or (
                    row + 1 < rows
                    and board[row + 1][col] != "\0"
                    and search(row + 1, col, index + 1)
                )
                or (
                    col > 0
                    and board[row][col - 1] != "\0"
                    and search(row, col - 1, index + 1)
                )
                or (
                    col + 1 < cols
                    and board[row][col + 1] != "\0"
                    and search(row, col + 1, index + 1)
                )
            )
            board[row][col] = char
            return found

        return any(search(row, col, 0) for row in range(rows) for col in range(cols))
