class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        best = 0
        for left in range(len(colors)):
            for right in range(left + 1, len(colors)):
                if colors[left] != colors[right]:
                    best = max(best, right - left)
        return best
