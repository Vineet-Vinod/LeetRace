class Solution:
    def leastBricks(self, wall: list[list[int]]) -> int:
        edges = Counter()
        for row in wall:
            position = 0
            for brick in row[:-1]:
                position += brick
                edges[position] += 1
        return len(wall) - max(edges.values(), default=0)
