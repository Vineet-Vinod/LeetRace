class Solution:
    def numDecodings(self, s: str) -> int:
        previous, current = 1, 1
        last = ""
        for c in s:
            single = 9 if c == "*" else int(c != "0")
            pair = 0
            if last == "*":
                pair = 15 if c == "*" else (2 if c <= "6" else 1)
            elif last == "1":
                pair = 9 if c == "*" else 1
            elif last == "2":
                pair = 6 if c == "*" else int(c <= "6")
            previous, current = (
                current,
                (current * single + previous * pair) % 1000000007,
            )
            last = c
        return current
