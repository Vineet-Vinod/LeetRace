class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total = 0
        smallest = inf
        negatives = 0
        for row in matrix:
            for value in row:
                total += abs(value)
                smallest = min(smallest, abs(value))
                negatives += value < 0
        return total if negatives % 2 == 0 else total - 2 * int(smallest)
