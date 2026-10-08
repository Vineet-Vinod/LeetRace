class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        return (
            [value for value in nums if value < pivot]
            + [value for value in nums if value == pivot]
            + [value for value in nums if value > pivot]
        )
