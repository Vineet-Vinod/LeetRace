class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        first, second = pattern
        first_count = 0
        pairs = 0
        second_count = 0
        for char in text:
            if char == second:
                pairs += first_count
                second_count += 1
            if char == first:
                first_count += 1
        return pairs + max(first_count, second_count)
