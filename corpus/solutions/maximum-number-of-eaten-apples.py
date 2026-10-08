from heapq import heappop, heappush


class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        heap: list[tuple[int, int]] = []
        eaten = 0
        day = 0
        while day < len(apples) or heap:
            if day < len(apples) and apples[day] > 0:
                heappush(heap, (day + days[day], apples[day]))
            while heap and (heap[0][0] <= day or heap[0][1] == 0):
                heappop(heap)
            if heap:
                expiry, count = heappop(heap)
                eaten += 1
                if count > 1:
                    heappush(heap, (expiry, count - 1))
            day += 1
        return eaten
