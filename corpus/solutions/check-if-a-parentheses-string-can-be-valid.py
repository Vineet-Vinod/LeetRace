class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2:
            return False
        low = 0
        high = 0
        for char, fixed in zip(s, locked):
            if fixed == "0":
                low -= 1
                high += 1
            elif char == "(":
                low += 1
                high += 1
            else:
                low -= 1
                high -= 1
            if high < 0:
                return False
            low = max(low, 0)
        return low == 0
