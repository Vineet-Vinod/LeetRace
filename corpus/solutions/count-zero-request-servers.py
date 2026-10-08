from collections import defaultdict


class Solution:
    def countServers(
        self, n: int, logs: List[List[int]], x: int, queries: List[int]
    ) -> List[int]:
        ordered_logs = sorted(logs, key=lambda log: log[1])
        ordered_queries = sorted((query, index) for index, query in enumerate(queries))
        counts: dict[int, int] = defaultdict(int)
        answer = [0] * len(queries)
        left = right = active = 0
        for query, index in ordered_queries:
            lower = query - x
            while right < len(ordered_logs) and ordered_logs[right][1] <= query:
                server = ordered_logs[right][0]
                if counts[server] == 0:
                    active += 1
                counts[server] += 1
                right += 1
            while left < right and ordered_logs[left][1] < lower:
                server = ordered_logs[left][0]
                counts[server] -= 1
                if counts[server] == 0:
                    active -= 1
                left += 1
            answer[index] = n - active
        return answer
