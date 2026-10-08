class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        queue = deque([root])
        result: List[List[int]] = []
        left_to_right = True
        while queue:
            level: List[int] = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            if not left_to_right:
                level.reverse()
            result.append(level)
            left_to_right = not left_to_right
        return result
