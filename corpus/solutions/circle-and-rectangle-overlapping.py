class Solution:
    def checkOverlap(
        self,
        radius: int,
        xCenter: int,
        yCenter: int,
        x1: int,
        y1: int,
        x2: int,
        y2: int,
    ) -> bool:
        nearest_x = min(max(xCenter, x1), x2)
        nearest_y = min(max(yCenter, y1), y2)
        return (nearest_x - xCenter) ** 2 + (
            nearest_y - yCenter
        ) ** 2 <= radius * radius
