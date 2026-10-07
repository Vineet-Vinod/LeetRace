class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        def distances(start: int) -> list[int]:
            result = [-1] * len(edges)
            distance = 0
            node = start
            while node != -1 and result[node] == -1:
                result[node] = distance
                distance += 1
                node = edges[node]
            return result

        first = distances(node1)
        second = distances(node2)
        candidates = [
            node for node in range(len(edges)) if first[node] >= 0 and second[node] >= 0
        ]
        if not candidates:
            return -1
        return min(candidates, key=lambda node: (max(first[node], second[node]), node))
