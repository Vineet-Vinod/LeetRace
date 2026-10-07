class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        ordered = sorted((max(abs(x), abs(y)), s[i]) for i, (x, y) in enumerate(points))
        seen = set()
        count = 0
        index = 0
        while index < len(ordered):
            boundary = ordered[index][0]
            end = index
            while end < len(ordered) and ordered[end][0] == boundary:
                end += 1
            labels = [label for _, label in ordered[index:end]]
            if len(labels) != len(set(labels)) or any(
                label in seen for label in labels
            ):
                break
            seen.update(labels)
            count = end
            index = end
        return count
