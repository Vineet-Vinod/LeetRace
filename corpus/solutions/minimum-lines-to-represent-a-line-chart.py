class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        points = sorted(stockPrices)
        if len(points) < 2:
            return 0
        answer = 1
        for i in range(2, len(points)):
            dx1 = points[i - 1][0] - points[i - 2][0]
            dy1 = points[i - 1][1] - points[i - 2][1]
            dx2 = points[i][0] - points[i - 1][0]
            dy2 = points[i][1] - points[i - 1][1]
            if dy1 * dx2 != dy2 * dx1:
                answer += 1
        return answer
