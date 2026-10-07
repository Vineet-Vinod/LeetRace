class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        depth = 0
        result = []
        for char in s:
            if char == "(":
                if depth:
                    result.append(char)
                depth += 1
            else:
                depth -= 1
                if depth:
                    result.append(char)
        return "".join(result)
