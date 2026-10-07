class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        values = sorted(arr)
        difference = values[1] - values[0]
        return all(
            values[i] - values[i - 1] == difference for i in range(2, len(values))
        )
