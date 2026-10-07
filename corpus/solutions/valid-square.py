class Solution:
    def validSquare(
        self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]
    ) -> bool:
        points = (p1, p2, p3, p4)
        distances = sorted(
            (
                (points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2
                for i in range(4)
                for j in range(i + 1, 4)
            )
        )
        return (
            distances[0] > 0
            and distances[:4] == [distances[0]] * 4
            and distances[4:] == [2 * distances[0]] * 2
        )
