class Solution:
    def countPoints(
        self, points: List[List[int]], queries: List[List[int]]
    ) -> List[int]:
        answer = []
        for x, y, radius in queries:
            squared = radius * radius
            answer.append(
                sum((px - x) ** 2 + (py - y) ** 2 <= squared for px, py in points)
            )
        return answer
