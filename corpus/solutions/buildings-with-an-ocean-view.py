class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        visible = []
        tallest = 0
        for index in range(len(heights) - 1, -1, -1):
            if heights[index] > tallest:
                visible.append(index)
                tallest = heights[index]
        return visible[::-1]
