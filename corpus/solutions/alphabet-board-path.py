class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        row = 0
        col = 0
        path: list[str] = []
        for letter in target:
            index = ord(letter) - ord("a")
            next_row, next_col = divmod(index, 5)
            if letter == "z":
                path.extend("L" * max(0, col - next_col))
                path.extend("U" * max(0, row - next_row))
                path.extend("D" * max(0, next_row - row))
                path.extend("R" * max(0, next_col - col))
            else:
                path.extend("U" * max(0, row - next_row))
                path.extend("L" * max(0, col - next_col))
                path.extend("D" * max(0, next_row - row))
                path.extend("R" * max(0, next_col - col))
            path.append("!")
            row, col = next_row, next_col
        return "".join(path)
