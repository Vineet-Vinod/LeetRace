class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack: list[str] = []
        for char in s:
            stack.append(char)
            if len(stack) >= len(part) and "".join(stack[-len(part) :]) == part:
                del stack[-len(part) :]
        return "".join(stack)
