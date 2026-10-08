class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        counts = sorted(word.count(char) for char in set(word))
        best = len(word)
        for minimum in counts:
            maximum = minimum + k
            deletions = sum(count for count in counts if count < minimum)
            deletions += sum(count - maximum for count in counts if count > maximum)
            best = min(best, deletions)
        return best
