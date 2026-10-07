class Solution:
    def findPattern(
        self, board: List[List[int]], pattern: List[List[str]]
    ) -> List[int]:
        rows, cols = len(board), len(board[0])
        height, width = len(pattern), len(pattern[0])
        fixed_values = {
            int(token) for row in pattern for token in row if token.isdigit()
        }
        for top in range(rows - height + 1):
            for left in range(cols - width + 1):
                letter_values = {}
                used_values = set()
                matched = True
                for r in range(height):
                    for c in range(width):
                        token = pattern[r][c]
                        value = board[top + r][left + c]
                        if token.isdigit():
                            if value != int(token):
                                matched = False
                                break
                        elif token in letter_values:
                            if letter_values[token] != value:
                                matched = False
                                break
                        else:
                            if value in used_values or value in fixed_values:
                                matched = False
                                break
                            letter_values[token] = value
                            used_values.add(value)
                    if not matched:
                        break
                if matched:
                    return [top, left]
        return [-1, -1]
