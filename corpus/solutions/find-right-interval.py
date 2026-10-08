class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        starts = sorted((start, i) for i, (start, _) in enumerate(intervals))
        values = [start for start, _ in starts]
        answer: list[int] = []
        for _, end in intervals:
            position = bisect_left(values, end)
            answer.append(starts[position][1] if position < len(starts) else -1)
        return answer
