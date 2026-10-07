class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        sums = {0}
        for row in mat:
            sums = {current + value for current in sums for value in row}
            if min(sums) >= target:
                return min(sums) - target
        return min(abs(value - target) for value in sums)
