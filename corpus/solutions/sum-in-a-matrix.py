class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        rows = [sorted(row) for row in nums]
        return sum(max(row[col] for row in rows) for col in range(len(rows[0])))
