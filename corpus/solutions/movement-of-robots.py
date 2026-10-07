class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        mod = 10**9 + 7
        positions = sorted(
            position + (d if direction == "R" else -d)
            for position, direction in zip(nums, s)
        )
        total = 0
        prefix = 0
        for index, position in enumerate(positions):
            total = (total + position * index - prefix) % mod
            prefix += position
        return total
