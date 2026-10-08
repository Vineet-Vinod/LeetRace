class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        free = [(weight, index) for index, weight in enumerate(servers)]
        heapify(free)
        busy: list[tuple[int, int, int]] = []
        assignments = []
        for time, duration in enumerate(tasks):
            while busy and busy[0][0] <= time:
                _, weight, index = heappop(busy)
                heappush(free, (weight, index))
            if not free:
                time = busy[0][0]
                while busy and busy[0][0] <= time:
                    _, weight, index = heappop(busy)
                    heappush(free, (weight, index))
            weight, index = heappop(free)
            assignments.append(index)
            heappush(busy, (time + duration, weight, index))
        return assignments
