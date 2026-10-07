class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_needed = 0
        insertions = 0
        for char in s:
            if char == "(":
                open_needed += 1
            elif open_needed:
                open_needed -= 1
            else:
                insertions += 1
        return insertions + open_needed
