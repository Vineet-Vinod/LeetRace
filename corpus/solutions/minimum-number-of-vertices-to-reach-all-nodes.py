class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        has_parent = [False] * n
        for _, destination in edges:
            has_parent[destination] = True
        return [node for node, incoming in enumerate(has_parent) if not incoming]
