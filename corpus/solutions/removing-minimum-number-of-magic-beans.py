class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        ordered = sorted(beans)
        total = sum(ordered)
        return min(
            total - value * (len(ordered) - index)
            for index, value in enumerate(ordered)
        )
