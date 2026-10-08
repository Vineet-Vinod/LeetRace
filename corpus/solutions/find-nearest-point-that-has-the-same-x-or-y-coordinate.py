class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        best_distance = None
        best_index = -1
        for index, (a, b) in enumerate(points):
            if a == x or b == y:
                distance = abs(a - x) + abs(b - y)
                if best_distance is None or distance < best_distance:
                    best_distance, best_index = distance, index
        return best_index
