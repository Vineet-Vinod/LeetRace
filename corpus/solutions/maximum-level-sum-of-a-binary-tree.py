from collections import deque


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        level = 0
        best_level = 1
        best_sum: int | None = None
        while queue:
            level += 1
            total = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                total += node.val
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            if best_sum is None or total > best_sum:
                best_sum = total
                best_level = level
        return best_level
