class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        sides = [min(length, width) for length, width in rectangles]
        return sides.count(max(sides))
