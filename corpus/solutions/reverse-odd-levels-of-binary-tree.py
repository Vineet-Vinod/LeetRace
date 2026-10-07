class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        queue = deque([root])
        level = 0
        while queue:
            nodes = [queue.popleft() for _ in range(len(queue))]
            if level % 2 == 1:
                values = [node.val for node in nodes][::-1]
                for node, value in zip(nodes, values):
                    node.val = value
            for node in nodes:
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            level += 1
        return root
