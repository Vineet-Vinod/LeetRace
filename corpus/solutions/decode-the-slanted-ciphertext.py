class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if not encodedText:
            return ""
        cols = len(encodedText) // rows
        decoded: list[str] = []
        for start_col in range(cols):
            row, col = 0, start_col
            while row < rows and col < cols:
                decoded.append(encodedText[row * cols + col])
                row += 1
                col += 1
        return "".join(decoded).rstrip()
