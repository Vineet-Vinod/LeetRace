from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def findCrossingTime(self, n: int, k: int, time: List[List[int]]) -> int:
        left = [(-(t[0] + t[2]), -i) for i, t in enumerate(time)]
        heapify(left)
        right = []
        picking = []
        putting = []
        now = 0
        remaining = n
        while remaining or right or picking:
            while picking and picking[0][0] <= now:
                _, i = heappop(picking)
                heappush(right, (-(time[i][0] + time[i][2]), -i))
            while putting and putting[0][0] <= now:
                _, i = heappop(putting)
                heappush(left, (-(time[i][0] + time[i][2]), -i))
            if right:
                _, negative_i = heappop(right)
                i = -negative_i
                now += time[i][2]
                heappush(putting, (now + time[i][3], i))
            elif remaining and left:
                _, negative_i = heappop(left)
                i = -negative_i
                remaining -= 1
                now += time[i][0]
                heappush(picking, (now + time[i][1], i))
            else:
                events = [picking[0][0]] if picking else []
                if remaining and putting:
                    events.append(putting[0][0])
                now = min(events)
        return now
