class Solution:
    def validateBinaryTreeNodes(
        self, n: int, leftChild: List[int], rightChild: List[int]
    ) -> bool:
        indegree = [0] * n
        for child in leftChild + rightChild:
            if child != -1:
                indegree[child] += 1
                if indegree[child] > 1:
                    return False
        roots = [node for node, degree in enumerate(indegree) if degree == 0]
        if len(roots) != 1:
            return False
        visited = set()
        queue = [roots[0]]
        for node in queue:
            if node in visited:
                return False
            visited.add(node)
            for child in (leftChild[node], rightChild[node]):
                if child != -1:
                    queue.append(child)
        return len(visited) == n
