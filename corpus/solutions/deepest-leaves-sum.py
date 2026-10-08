class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        total = 0
        while queue:
            total = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                total += node.val
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
        return total
