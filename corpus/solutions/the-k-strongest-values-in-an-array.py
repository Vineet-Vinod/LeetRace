class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        ordered = sorted(arr)
        median = ordered[(len(arr) - 1) // 2]
        ranked = sorted(
            arr, key=lambda value: (abs(value - median), value), reverse=True
        )
        return ranked[:k]
