class Solution:
    def minInsertions(self, s: str) -> int:
        insertions = 0
        needed_closes = 0
        for char in s:
            if char == "(":
                if needed_closes % 2:
                    insertions += 1
                    needed_closes -= 1
                needed_closes += 2
            else:
                needed_closes -= 1
                if needed_closes < 0:
                    insertions += 1
                    needed_closes = 1
        return insertions + needed_closes
