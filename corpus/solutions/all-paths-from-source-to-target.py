class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths: list[list[int]] = []
        path = [0]
        target = len(graph) - 1

        def visit(node: int) -> None:
            if node == target:
                paths.append(path.copy())
                return
            for neighbor in sorted(graph[node]):
                path.append(neighbor)
                visit(neighbor)
                path.pop()

        visit(0)
        return paths
