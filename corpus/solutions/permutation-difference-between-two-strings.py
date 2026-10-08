class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        positions = {char: index for index, char in enumerate(t)}
        return sum(abs(index - positions[char]) for index, char in enumerate(s))
