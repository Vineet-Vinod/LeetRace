class Solution:
    def minimumDeletions(self, s: str) -> int:
        deletions = 0
        b_count = 0
        for char in s:
            if char == "a":
                deletions = min(deletions + 1, b_count)
            else:
                b_count += 1
        return deletions
