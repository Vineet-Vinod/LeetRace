class Solution:
    def countPoints(self, rings: str) -> int:
        rods = [set() for _ in range(10)]
        for index in range(0, len(rings), 2):
            rods[int(rings[index + 1])].add(rings[index])
        return sum(len(colors) == 3 for colors in rods)
