class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        queue = deque([root])
        answer = []
        while queue:
            largest = -inf
            for _ in range(len(queue)):
                node = queue.popleft()
                largest = max(largest, node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            answer.append(largest)
        return answer
