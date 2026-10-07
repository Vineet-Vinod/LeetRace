class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        count = 0
        for ax, ay in points:
            for bx, by in points:
                if ax > bx or ay < by or (ax == bx and ay == by):
                    continue
                if all(
                    not (ax <= x <= bx and by <= y <= ay)
                    or (x, y) in ((ax, ay), (bx, by))
                    for x, y in points
                ):
                    count += 1
        return count
