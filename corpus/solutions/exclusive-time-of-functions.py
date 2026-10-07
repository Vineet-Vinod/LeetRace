class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        totals = [0] * n
        stack: list[int] = []
        previous_time = 0
        for log in logs:
            function_text, kind, time_text = log.split(":")
            function_id = int(function_text)
            timestamp = int(time_text)
            if kind == "start":
                if stack:
                    totals[stack[-1]] += timestamp - previous_time
                stack.append(function_id)
                previous_time = timestamp
            else:
                totals[stack.pop()] += timestamp - previous_time + 1
                previous_time = timestamp + 1
        return totals
