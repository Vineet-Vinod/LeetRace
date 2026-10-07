class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        width = math.isqrt(area)
        while area % width:
            width -= 1
        return [area // width, width]
