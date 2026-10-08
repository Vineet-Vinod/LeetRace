from collections import deque


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        visible: list[int] = []
        queue = deque([root])
        while queue:
            width = len(queue)
            for index in range(width):
                node = queue.popleft()
                if index == width - 1:
                    visible.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
        return visible
