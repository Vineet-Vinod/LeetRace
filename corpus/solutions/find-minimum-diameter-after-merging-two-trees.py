from typing import List


class Solution:
    def minimumDiameterAfterMerge(
        self, edges1: List[List[int]], edges2: List[List[int]]
    ) -> int:
        def diameter(edges):
            graph = [[] for _ in range(len(edges) + 1)]
            for a, b in edges:
                graph[a].append(b)
                graph[b].append(a)

            def farthest(start):
                queue = [(start, -1, 0)]
                end, distance = start, 0
                for u, parent, depth in queue:
                    if depth > distance:
                        end, distance = u, depth
                    queue.extend((v, u, depth + 1) for v in graph[u] if v != parent)
                return end, distance

            return farthest(farthest(0)[0])[1]

        a, b = diameter(edges1), diameter(edges2)
        return max(a, b, (a + 1) // 2 + (b + 1) // 2 + 1)
