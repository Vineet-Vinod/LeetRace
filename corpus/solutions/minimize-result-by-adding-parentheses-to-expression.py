class Solution:
    def minimizeResult(self, expression: str) -> str:
        plus = expression.index("+")
        left, right = expression[:plus], expression[plus + 1 :]
        best_value: int | None = None
        best_expression = ""
        for start in range(len(left)):
            for end in range(1, len(right) + 1):
                prefix = int(left[:start]) if start else 1
                middle = int(left[start:]) + int(right[:end])
                suffix = int(right[end:]) if end < len(right) else 1
                value = prefix * middle * suffix
                candidate = (
                    left[:start]
                    + "("
                    + left[start:]
                    + "+"
                    + right[:end]
                    + ")"
                    + right[end:]
                )
                if (
                    best_value is None
                    or value < best_value
                    or (value == best_value and candidate < best_expression)
                ):
                    best_value = value
                    best_expression = candidate
        return best_expression
