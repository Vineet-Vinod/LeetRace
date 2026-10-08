class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        def height(first: int, second: int) -> int:
            rows = 0
            balls = 1
            while True:
                available = first if rows % 2 == 0 else second
                if available < balls:
                    return rows
                first, second = (
                    (first - balls, second)
                    if rows % 2 == 0
                    else (first, second - balls)
                )
                rows += 1
                balls += 1

        return max(height(red, blue), height(blue, red))
