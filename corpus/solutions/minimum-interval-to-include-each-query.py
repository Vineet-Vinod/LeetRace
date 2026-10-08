from typing import List
from heapq import heappush, heappop


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        spans = sorted(intervals)
        heap = []
        answers = {}
        i = 0
        for query in sorted(set(queries)):
            while i < len(spans) and spans[i][0] <= query:
                left, right = spans[i]
                heappush(heap, (right - left + 1, right))
                i += 1
            while heap and heap[0][1] < query:
                heappop(heap)
            answers[query] = heap[0][0] if heap else -1
        return [answers[query] for query in queries]
