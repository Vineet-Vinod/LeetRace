class Solution:
    def minJumps(self, arr: List[int]) -> int:
        positions = defaultdict(list)
        for index, value in enumerate(arr):
            positions[value].append(index)
        queue = deque([(0, 0)])
        visited = {0}
        while queue:
            index, steps = queue.popleft()
            if index == len(arr) - 1:
                return steps
            for neighbor in [index - 1, index + 1] + positions.pop(arr[index], []):
                if 0 <= neighbor < len(arr) and neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, steps + 1))
        return -1
