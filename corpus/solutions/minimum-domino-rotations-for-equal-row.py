class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        def rotations(value: int) -> int:
            top_count = bottom_count = 0
            for top, bottom in zip(tops, bottoms):
                if top != value and bottom != value:
                    return len(tops) + 1
                top_count += top == value
                bottom_count += bottom == value
            return min(len(tops) - top_count, len(tops) - bottom_count)

        best = min(rotations(tops[0]), rotations(bottoms[0]))
        return best if best <= len(tops) else -1
