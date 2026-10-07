class Solution:
    def getOrder(self, tasks: list[list[int]]) -> list[int]:
        ordered = sorted(
            (enqueue, duration, index)
            for index, (enqueue, duration) in enumerate(tasks)
        )
        ready: list[tuple[int, int]] = []
        result = []
        time = task_index = 0
        while task_index < len(tasks) or ready:
            if not ready and time < ordered[task_index][0]:
                time = ordered[task_index][0]
            while task_index < len(tasks) and ordered[task_index][0] <= time:
                _, duration, original_index = ordered[task_index]
                heappush(ready, (duration, original_index))
                task_index += 1
            duration, original_index = heappop(ready)
            time += duration
            result.append(original_index)
        return result
