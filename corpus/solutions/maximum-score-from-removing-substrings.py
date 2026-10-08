class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove(text: str, first: str, second: str, score: int) -> Tuple[str, int]:
            stack = []
            total = 0
            for char in text:
                if stack and stack[-1] == first and char == second:
                    stack.pop()
                    total += score
                else:
                    stack.append(char)
            return "".join(stack), total

        if x >= y:
            remaining, score = remove(s, "a", "b", x)
            _, extra = remove(remaining, "b", "a", y)
        else:
            remaining, score = remove(s, "b", "a", y)
            _, extra = remove(remaining, "a", "b", x)
        return score + extra
