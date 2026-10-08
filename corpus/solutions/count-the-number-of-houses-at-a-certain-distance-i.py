class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        answer = [0] * n
        for start in range(1, n + 1):
            distances = [n] * (n + 1)
            distances[start] = 0
            queue = deque([start])
            while queue:
                node = queue.popleft()
                neighbors = []
                if node > 1:
                    neighbors.append(node - 1)
                if node < n:
                    neighbors.append(node + 1)
                if node == x:
                    neighbors.append(y)
                if node == y:
                    neighbors.append(x)
                for neighbor in neighbors:
                    if distances[neighbor] == n:
                        distances[neighbor] = distances[node] + 1
                        queue.append(neighbor)
            for target in range(start + 1, n + 1):
                answer[distances[target] - 1] += 2
        return answer
