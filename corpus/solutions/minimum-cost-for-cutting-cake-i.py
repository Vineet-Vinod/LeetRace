class Solution:
    def minimumCost(
        self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]
    ) -> int:
        cuts = sorted(
            [(x, 0) for x in horizontalCut] + [(x, 1) for x in verticalCut],
            reverse=True,
        )
        horizontal_pieces = vertical_pieces = 1
        total = 0
        for cost, direction in cuts:
            if direction == 0:
                total += cost * vertical_pieces
                horizontal_pieces += 1
            else:
                total += cost * horizontal_pieces
                vertical_pieces += 1
        return total
