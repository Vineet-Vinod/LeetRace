class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        rows = len(board)
        cols = len(board[0])
        while True:
            crushed = [[False] * cols for _ in range(rows)]
            found = False
            for row in range(rows):
                for col in range(cols - 2):
                    value = board[row][col]
                    if value and value == board[row][col + 1] == board[row][col + 2]:
                        end = col + 3
                        while end < cols and board[row][end] == value:
                            end += 1
                        for index in range(col, end):
                            crushed[row][index] = True
                        found = True
            for col in range(cols):
                for row in range(rows - 2):
                    value = board[row][col]
                    if value and value == board[row + 1][col] == board[row + 2][col]:
                        end = row + 3
                        while end < rows and board[end][col] == value:
                            end += 1
                        for index in range(row, end):
                            crushed[index][col] = True
                        found = True
            if not found:
                return board
            for col in range(cols):
                write = rows - 1
                for read in range(rows - 1, -1, -1):
                    if not crushed[read][col] and board[read][col] != 0:
                        board[write][col] = board[read][col]
                        write -= 1
                while write >= 0:
                    board[write][col] = 0
                    write -= 1
