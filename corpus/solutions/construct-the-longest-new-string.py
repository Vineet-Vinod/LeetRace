class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        return 4 * min(x, y) + 2 * z + 2 * (x != y)
