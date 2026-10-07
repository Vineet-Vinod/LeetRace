class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        parents = [[] for _ in range(n)]
        for source, target in edges:
            parents[target].append(source)
        result = []
        for node in range(n):
            found = set()
            stack = parents[node][:]
            while stack:
                current = stack.pop()
                if current not in found:
                    found.add(current)
                    stack.extend(parents[current])
            result.append(sorted(found))
        return result
