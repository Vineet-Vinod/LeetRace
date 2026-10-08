class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        best_id = logs[0][0]
        best_duration = logs[0][1]
        previous_time = logs[0][1]
        for employee, leave_time in logs[1:]:
            duration = leave_time - previous_time
            if duration > best_duration or (
                duration == best_duration and employee < best_id
            ):
                best_duration, best_id = duration, employee
            previous_time = leave_time
        return best_id
