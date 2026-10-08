class Solution:
    def minimumCost(
        self, m: int, n: int, horizontalCut: list[int], verticalCut: list[int]
    ) -> int:
        cuts = [(x, 0) for x in horizontalCut] + [(x, 1) for x in verticalCut]
        cuts.sort(reverse=True)
        pieces = [1, 1]
        total = 0
        for cost, direction in cuts:
            total += cost * pieces[1 - direction]
            pieces[direction] += 1
        return total
