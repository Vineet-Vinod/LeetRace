class Solution:
    def countPairsOfConnectableServers(
        self, edges: List[List[int]], signalSpeed: int
    ) -> List[int]:
        n = len(edges) + 1
        graph: List[List[Tuple[int, int]]] = [[] for _ in range(n)]
        for a, b, weight in edges:
            graph[a].append((b, weight))
            graph[b].append((a, weight))
        answer = []
        for center in range(n):
            total = 0
            pairs = 0
            for neighbor, weight in graph[center]:
                count = 0
                stack = [(neighbor, center, weight)]
                while stack:
                    node, parent, distance = stack.pop()
                    if distance % signalSpeed == 0:
                        count += 1
                    for nxt, edge_weight in graph[node]:
                        if nxt != parent:
                            stack.append((nxt, node, distance + edge_weight))
                pairs += total * count
                total += count
            answer.append(pairs)
        return answer
