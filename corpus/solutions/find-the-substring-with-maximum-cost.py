class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        costs = {char: value for char, value in zip(chars, vals)}
        best = 0
        ending_here = 0
        for char in s:
            ending_here = max(
                0, ending_here + costs.get(char, ord(char) - ord("a") + 1)
            )
            best = max(best, ending_here)
        return best
