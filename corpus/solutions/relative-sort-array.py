class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        order = {value: index for index, value in enumerate(arr2)}
        return sorted(
            arr1, key=lambda value: (0, order[value]) if value in order else (1, value)
        )
