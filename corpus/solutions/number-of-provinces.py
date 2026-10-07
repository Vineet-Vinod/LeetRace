class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        seen = set()
        components = 0
        for start in range(n):
            if start in seen:
                continue
            components += 1
            stack = [start]
            seen.add(start)
            while stack:
                node = stack.pop()
                for neighbor, connected in enumerate(isConnected[node]):
                    if connected and neighbor not in seen:
                        seen.add(neighbor)
                        stack.append(neighbor)
        return components
