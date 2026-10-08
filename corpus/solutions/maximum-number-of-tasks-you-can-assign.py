class Solution:
    def maxTaskAssign(
        self, tasks: List[int], workers: List[int], pills: int, strength: int
    ) -> int:
        tasks = sorted(tasks)
        workers = sorted(workers)

        def feasible(count):
            available = deque()
            index = len(workers) - 1
            remaining = pills
            for task in reversed(tasks[:count]):
                while (
                    index >= len(workers) - count and workers[index] + strength >= task
                ):
                    available.appendleft(workers[index])
                    index -= 1
                if not available:
                    return False
                if available[-1] >= task:
                    available.pop()
                elif remaining:
                    remaining -= 1
                    available.popleft()
                else:
                    return False
            return True

        low, high = 0, min(len(tasks), len(workers))
        while low < high:
            middle = (low + high + 1) // 2
            if feasible(middle):
                low = middle
            else:
                high = middle - 1
        return low
