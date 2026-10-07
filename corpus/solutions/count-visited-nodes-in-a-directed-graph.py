from typing import List


class Solution:
    def countVisitedNodes(self, edges: List[int]) -> List[int]:
        from collections import deque

        n = len(edges)
        indegree = [0] * n
        for target in edges:
            indegree[target] += 1
        queue = deque(i for i, value in enumerate(indegree) if value == 0)
        removed = []
        while queue:
            node = queue.popleft()
            removed.append(node)
            target = edges[node]
            indegree[target] -= 1
            if indegree[target] == 0:
                queue.append(target)
        answer = [0] * n
        for node in range(n):
            if indegree[node] and not answer[node]:
                cycle = [node]
                target = edges[node]
                while target != node:
                    cycle.append(target)
                    target = edges[target]
                for member in cycle:
                    answer[member] = len(cycle)
        for node in reversed(removed):
            answer[node] = answer[edges[node]] + 1
        return answer
