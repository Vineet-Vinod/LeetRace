class Solution:
    def reformatNumber(self, number: str) -> str:
        digits = "".join(char for char in number if char.isdigit())
        blocks = []
        index = 0
        while len(digits) - index > 4:
            blocks.append(digits[index : index + 3])
            index += 3
        remaining = digits[index:]
        if len(remaining) == 4:
            blocks.extend([remaining[:2], remaining[2:]])
        elif remaining:
            blocks.append(remaining)
        return "-".join(blocks)
