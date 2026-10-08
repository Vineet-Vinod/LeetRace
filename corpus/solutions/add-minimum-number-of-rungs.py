class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        added = 0
        previous = 0
        for height in rungs:
            gap = height - previous
            added += (gap - 1) // dist
            previous = height
        return added
