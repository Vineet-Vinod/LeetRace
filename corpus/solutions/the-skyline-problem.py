from typing import List
import heapq


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = {}
        for left, right, h in buildings:
            events.setdefault(left, []).append((-h, right))
            events.setdefault(right, [])
        heap = [(0, 10**30)]
        ans = []
        for x in sorted(events):
            for event in events[x]:
                heapq.heappush(heap, event)
            while heap[0][1] <= x:
                heapq.heappop(heap)
            h = -heap[0][0]
            if not ans or ans[-1][1] != h:
                ans.append([x, h])
        return ans
