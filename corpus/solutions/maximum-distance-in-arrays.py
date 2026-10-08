class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        smallest = arrays[0][0]
        largest = arrays[0][-1]
        best = 0
        for values in arrays[1:]:
            best = max(best, values[-1] - smallest, largest - values[0])
            smallest = min(smallest, values[0])
            largest = max(largest, values[-1])
        return best
