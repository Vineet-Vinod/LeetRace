class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged: List[List[int]] = []
        for start, end in sorted(intervals):
            if not merged or start > merged[-1][1]:
                merged.append([start, end])
            else:
                merged[-1][1] = max(merged[-1][1], end)
        return merged
