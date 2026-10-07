import heapq


class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        heap = []
        total = 0
        for duration, deadline in sorted(courses, key=lambda x: x[1]):
            total += duration
            heapq.heappush(heap, -duration)
            if total > deadline:
                total += heapq.heappop(heap)
        return len(heap)
