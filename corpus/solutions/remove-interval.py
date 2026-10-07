class Solution:
    def removeInterval(
        self, intervals: List[List[int]], toBeRemoved: List[int]
    ) -> List[List[int]]:
        left, right = toBeRemoved
        result = []
        for start, end in intervals:
            if end <= left or start >= right:
                result.append([start, end])
            else:
                if start < left:
                    result.append([start, left])
                if end > right:
                    result.append([right, end])
        return result
