class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        positions: Dict[int, List[int]] = {}
        for index, value in enumerate(arr):
            positions.setdefault(value, []).append(index)
        result = [0] * len(arr)
        for indices in positions.values():
            prefix = 0
            total = sum(indices)
            for offset, index in enumerate(indices):
                left = index * offset - prefix
                right = (total - prefix - index) - index * (len(indices) - offset - 1)
                result[index] = left + right
                prefix += index
        return result
