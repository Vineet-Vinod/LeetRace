class Solution:
    def numberOfAlternatingGroups(self, colors: list[int]) -> int:
        size = len(colors)
        return sum(
            colors[i] != colors[(i + 1) % size]
            and colors[(i + 1) % size] != colors[(i + 2) % size]
            for i in range(size)
        )
