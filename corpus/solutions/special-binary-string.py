class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        def largest(text):
            balance = 0
            start = 0
            pieces = []
            for i, ch in enumerate(text):
                balance += 1 if ch == "1" else -1
                if balance == 0:
                    pieces.append("1" + largest(text[start + 1 : i]) + "0")
                    start = i + 1
            return "".join(sorted(pieces, reverse=True))

        return largest(s)
