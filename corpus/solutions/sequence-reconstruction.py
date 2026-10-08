class Solution:
    def sequenceReconstruction(
        self, nums: List[int], sequences: List[List[int]]
    ) -> bool:
        graph = {value: set() for value in nums}
        indegree = {value: 0 for value in nums}
        covered = set()
        for sequence in sequences:
            covered.update(sequence)
            for a, b in zip(sequence, sequence[1:]):
                if b not in graph[a]:
                    graph[a].add(b)
                    indegree[b] += 1
        if covered != set(nums):
            return False
        queue = deque(value for value in nums if indegree[value] == 0)
        for expected in nums:
            if len(queue) != 1 or queue[0] != expected:
                return False
            node = queue.popleft()
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        return True
