class Solution:
    def minChanges(self, s: str) -> int:
        changes = 0
        for index in range(0, len(s), 2):
            changes += s[index] != s[index + 1]
        return changes
