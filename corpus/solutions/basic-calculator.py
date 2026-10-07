class Solution:
    def calculate(self, s: str) -> int:
        total, sign, number = 0, 1, 0
        stack = []
        for ch in s:
            if ch.isdigit():
                number = number * 10 + int(ch)
            elif ch in "+-":
                total += sign * number
                number = 0
                sign = 1 if ch == "+" else -1
            elif ch == "(":
                stack.append((total, sign))
                total, sign = 0, 1
            elif ch == ")":
                total += sign * number
                number = 0
                previous, multiplier = stack.pop()
                total = previous + multiplier * total
        return total + sign * number
