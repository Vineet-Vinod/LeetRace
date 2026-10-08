class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []
        for character in expression:
            if character == ",":
                continue
            if character != ")":
                stack.append(character)
                continue
            values = []
            while stack[-1] != "(":
                values.append(stack.pop() == "t")
            stack.pop()
            operator = stack.pop()
            value = (
                not values[0]
                if operator == "!"
                else all(values)
                if operator == "&"
                else any(values)
            )
            stack.append("t" if value else "f")
        return stack[0] == "t"
