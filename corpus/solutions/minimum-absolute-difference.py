class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        values = sorted(arr)
        difference = min(values[i + 1] - values[i] for i in range(len(values) - 1))
        return [
            [values[i], values[i + 1]]
            for i in range(len(values) - 1)
            if values[i + 1] - values[i] == difference
        ]
