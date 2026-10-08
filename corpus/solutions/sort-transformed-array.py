class Solution:
    def sortTransformedArray(
        self, nums: List[int], a: int, b: int, c: int
    ) -> List[int]:
        values = [a * value * value + b * value + c for value in nums]
        return sorted(values)
