class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        values = nums.copy()
        for index in range(len(values) - 1):
            if values[index] == values[index + 1]:
                values[index] *= 2
                values[index + 1] = 0
        nonzero = [value for value in values if value != 0]
        return nonzero + [0] * (len(values) - len(nonzero))
