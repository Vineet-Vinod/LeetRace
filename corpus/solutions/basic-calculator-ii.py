class Solution:
    def calculate(self, s: str) -> int:
        total = 0
        last = 0
        number = 0
        operator = "+"
        for i, ch in enumerate(s + "+"):
            if ch.isdigit():
                number = number * 10 + int(ch)
            if ch in "+-*/" or i == len(s):
                if operator == "+":
                    total += last
                    last = number
                elif operator == "-":
                    total += last
                    last = -number
                elif operator == "*":
                    last *= number
                else:
                    last = int(last / number)
                operator = ch
                number = 0
        return total + last
