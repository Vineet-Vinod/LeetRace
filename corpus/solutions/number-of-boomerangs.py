class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        total = 0
        for x, y in points:
            distances = Counter(
                (x - other_x) ** 2 + (y - other_y) ** 2 for other_x, other_y in points
            )
            total += sum(count * (count - 1) for count in distances.values())
        return total
