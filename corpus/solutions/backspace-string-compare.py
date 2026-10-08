class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def decoded(value: str) -> str:
            stack: list[str] = []
            for char in value:
                if char == "#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(char)
            return "".join(stack)

        return decoded(s) == decoded(t)
