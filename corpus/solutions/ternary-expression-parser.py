class Solution:
    def parseTernary(self, expression: str) -> str:
        stack = []
        index = len(expression) - 1
        while index >= 0:
            char = expression[index]
            if char == "?":
                true_value = stack.pop()
                false_value = stack.pop()
                stack.append(
                    true_value if expression[index - 1] == "T" else false_value
                )
                index -= 1
            elif char != ":":
                stack.append(char)
            index -= 1
        return stack[-1]
