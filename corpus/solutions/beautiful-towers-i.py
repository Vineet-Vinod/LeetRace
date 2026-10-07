class Solution:
    def maximumSumOfHeights(self, heights: List[int]) -> int:
        best = 0
        for peak in range(len(heights)):
            total = heights[peak]
            height = heights[peak]
            for i in range(peak - 1, -1, -1):
                height = min(height, heights[i])
                total += height
            height = heights[peak]
            for i in range(peak + 1, len(heights)):
                height = min(height, heights[i])
                total += height
            best = max(best, total)
        return best
