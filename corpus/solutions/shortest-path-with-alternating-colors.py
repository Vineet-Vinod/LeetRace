class Solution:
    def shortestAlternatingPaths(
        self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]
    ) -> List[int]:
        graphs = [defaultdict(list), defaultdict(list)]
        for a, b in redEdges:
            graphs[0][a].append(b)
        for a, b in blueEdges:
            graphs[1][a].append(b)
        distances = [[-1] * n for _ in range(2)]
        queue = deque([(0, 0), (0, 1)])
        distances[0][0] = distances[1][0] = 0
        while queue:
            node, previous_color = queue.popleft()
            next_color = 1 - previous_color
            for neighbor in graphs[next_color][node]:
                if distances[next_color][neighbor] == -1:
                    distances[next_color][neighbor] = (
                        distances[previous_color][node] + 1
                    )
                    queue.append((neighbor, next_color))
        answer = []
        for node in range(n):
            choices = [
                distance
                for distance in (distances[0][node], distances[1][node])
                if distance >= 0
            ]
            answer.append(min(choices) if choices else -1)
        return answer
