class Solution:
    def minimumLevel(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        best_sum = float("inf")
        best_level = 1
        level = 0
        while queue:
            level += 1
            total = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                total += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if total < best_sum:
                best_sum = total
                best_level = level
        return best_level
