class Solution:
    def minDistance(
        self,
        height: int,
        width: int,
        tree: List[int],
        squirrel: List[int],
        nuts: List[List[int]],
    ) -> int:
        def distance(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])

        baseline = sum(2 * distance(tree, nut) for nut in nuts)
        saving = max(distance(tree, nut) - distance(squirrel, nut) for nut in nuts)
        return baseline - saving
