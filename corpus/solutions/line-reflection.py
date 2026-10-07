class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        point_set = {tuple(point) for point in points}
        minimum = min(x for x, _ in points)
        maximum = max(x for x, _ in points)
        doubled_axis = minimum + maximum
        return all((doubled_axis - x, y) in point_set for x, y in point_set)
