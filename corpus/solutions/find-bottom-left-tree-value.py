class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        leftmost = root.val
        while queue:
            level_size = len(queue)
            for index in range(level_size):
                node = queue.popleft()
                if index == 0:
                    leftmost = node.val
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
        return leftmost
