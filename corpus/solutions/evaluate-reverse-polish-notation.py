class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack: list[int] = []
        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                right, left = stack.pop(), stack.pop()
                if token == "+":
                    value = left + right
                elif token == "-":
                    value = left - right
                elif token == "*":
                    value = left * right
                else:
                    value = (
                        abs(left)
                        // abs(right)
                        * (-1 if (left < 0) != (right < 0) else 1)
                    )
                stack.append(value)
            else:
                stack.append(int(token))
        return stack[0]
