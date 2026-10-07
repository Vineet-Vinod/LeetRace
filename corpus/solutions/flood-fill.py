class Solution:
    def floodFill(
        self, image: list[list[int]], sr: int, sc: int, color: int
    ) -> list[list[int]]:
        original = image[sr][sc]
        if original == color:
            return image
        rows, columns = len(image), len(image[0])
        stack = [(sr, sc)]
        image[sr][sc] = color
        while stack:
            row, column = stack.pop()
            for next_row, next_column in (
                (row - 1, column),
                (row + 1, column),
                (row, column - 1),
                (row, column + 1),
            ):
                if (
                    0 <= next_row < rows
                    and 0 <= next_column < columns
                    and image[next_row][next_column] == original
                ):
                    image[next_row][next_column] = color
                    stack.append((next_row, next_column))
        return image
