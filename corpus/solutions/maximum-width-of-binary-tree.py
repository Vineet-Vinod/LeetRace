from collections import deque


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = deque([(root, 0)])
        widest = 0
        while queue:
            level_size = len(queue)
            first_index = queue[0][1]
            last_index = first_index
            for _ in range(level_size):
                node, index = queue.popleft()
                normalized = index - first_index
                last_index = normalized
                if node.left is not None:
                    queue.append((node.left, normalized * 2))
                if node.right is not None:
                    queue.append((node.right, normalized * 2 + 1))
            widest = max(widest, last_index + 1)
        return widest
