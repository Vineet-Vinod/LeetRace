class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        present = set(nums)
        lengths: Dict[int, int] = {}
        best = 1
        for value in sorted(present):
            root = isqrt(value)
            lengths[value] = lengths.get(root, 0) + 1 if root * root == value else 1
            best = max(best, lengths[value])
        return best if best >= 2 else -1
