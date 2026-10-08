class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph: Dict[int, List[int]] = defaultdict(list)
        for a, b in adjacentPairs:
            graph[a].append(b)
            graph[b].append(a)
        endpoint = next(
            value for value, neighbors in graph.items() if len(neighbors) == 1
        )
        path = [endpoint]
        previous = None
        current = endpoint
        while len(path) < len(graph):
            nxt = next(value for value in graph[current] if value != previous)
            path.append(nxt)
            previous, current = current, nxt
        reverse = path[::-1]
        return min(path, reverse)
