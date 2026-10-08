class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        first, middle, last = sorted((a, b, c))
        left_gap = middle - first
        right_gap = last - middle
        maximum = left_gap + right_gap - 2
        if left_gap == 1 and right_gap == 1:
            minimum = 0
        elif left_gap <= 2 or right_gap <= 2:
            minimum = 1
        else:
            minimum = 2
        return [minimum, maximum]
