class Solution:
    def minMoves(self, rooks: List[List[int]]) -> int:
        len(rooks)
        rows = sorted(rook[0] for rook in rooks)
        cols = sorted(rook[1] for rook in rooks)
        return sum(abs(value - index) for index, value in enumerate(rows)) + sum(
            abs(value - index) for index, value in enumerate(cols)
        )
