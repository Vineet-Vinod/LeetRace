from heapq import heapify, heappush, heappop


class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        available = list(range(n))
        heapify(available)
        busy = []
        counts = [0] * n
        for start, end in sorted(meetings):
            while busy and busy[0][0] <= start:
                _, room = heappop(busy)
                heappush(available, room)
            if available:
                room = heappop(available)
                finish = end
            else:
                time, room = heappop(busy)
                finish = time + end - start
            counts[room] += 1
            heappush(busy, (finish, room))
        return max(range(n), key=lambda r: (counts[r], -r))
