class Solution:
    def minOperations(self, s: str) -> int:
        changes = sum(ch != ("0" if i % 2 == 0 else "1") for i, ch in enumerate(s))
        return min(changes, len(s) - changes)
