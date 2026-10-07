class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        ordered = sorted(points, key=lambda interval: interval[1])
        arrows = 0
        position = None
        for start, end in ordered:
            if position is None or start > position:
                arrows += 1
                position = end
        return arrows
