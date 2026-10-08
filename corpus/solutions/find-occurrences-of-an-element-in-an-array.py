class Solution:
    def occurrencesOfElement(
        self, nums: List[int], queries: List[int], x: int
    ) -> List[int]:
        positions = [i for i, value in enumerate(nums) if value == x]
        return [positions[q - 1] if q <= len(positions) else -1 for q in queries]
