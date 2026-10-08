class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        graph = [[] for _ in range(n)]
        for i, (x1, y1, radius) in enumerate(bombs):
            radius_squared = radius * radius
            for j, (x2, y2, _) in enumerate(bombs):
                if i != j and (x1 - x2) ** 2 + (y1 - y2) ** 2 <= radius_squared:
                    graph[i].append(j)
        answer = 0
        for start in range(n):
            seen = {start}
            stack = [start]
            while stack:
                node = stack.pop()
                for neighbor in graph[node]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        stack.append(neighbor)
            answer = max(answer, len(seen))
        return answer
