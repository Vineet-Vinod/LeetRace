class Solution:
    def findDiagonalOrder(self, nums: list[list[int]]) -> list[int]:
        diagonals: dict[int, list[int]] = {}
        for row, values in enumerate(nums):
            for col, value in enumerate(values):
                diagonals.setdefault(row + col, []).append(value)
        result = []
        for diagonal in range(max(diagonals) + 1):
            result.extend(reversed(diagonals[diagonal]))
        return result
